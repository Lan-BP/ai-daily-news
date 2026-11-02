import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import feishu_push
import html_generator


class DailySupplementTests(unittest.TestCase):
    def test_daily_card_keeps_all_thirteen_headlines(self):
        titles = [f'公司发布第{i}项独立进展' for i in range(1, 14)]
        summary = '<div class="summary"><div class="sum-cat">'
        summary += '<span class="sum-cat-name">产业动态</span>'
        summary += ''.join(f'<span class="sum-item">{t}</span>' for t in titles)
        summary += '</div></div><div class="layout">'
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'daily-ai-news-2026-11-03-supplement.html').write_text(summary)
            with patch.object(feishu_push, 'BASE_DIR', root):
                card = feishu_push.build_card('2026-11-03-supplement')

        self.assertEqual(card['header']['title']['content'], '2026-11-03 AI 前沿动态｜补刊')
        text = card['elements'][0]['text']['content']
        self.assertEqual(text.count('• '), 13)
        self.assertTrue(all(title in text for title in titles))
        self.assertEqual(card['elements'][-1]['actions'][0]['text']['content'], '查看日报')

    def test_supplement_archive_coexists_with_regular_issue_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = root / 'index.html'
            index.write_text('''<details class="nav-details" open>
                <summary><span>2026 年 11 月</span><span class="nav-count">0</span></summary>
                <div class="nav-articles"></div></details>
                <div class="month-group"><div class="month-body" id="month-nov"></div></div>''')
            with patch.object(html_generator, '__file__', str(root / 'html_generator.py')):
                html_generator._update_index_html('2026-11-03', [{'title': '常规日报原有内容'}])
                for _ in range(2):
                    html_generator._update_index_html(
                        '2026-11-03', [{'title': '近期补刊完整内容'}], edition='supplement'
                    )
                html_generator._update_index_html('2026-11-04', [{'title': '下一期常规日报'}])
            text = index.read_text()

        self.assertEqual(text.count('id="nov-3-supplement"'), 1)
        self.assertEqual(text.count('id="nov-3"'), 1)
        self.assertIn('常规日报原有内容', text)
        self.assertIn('daily-ai-news-2026-11-03-supplement.html', text)
        self.assertIn('href="#nov-3-supplement"', text)
        self.assertIn('Nov 03 · 补刊', text)
        self.assertIn('class="nav-count">3</span>', text)
        self.assertLess(text.index('id="nov-4"'), text.index('id="nov-3"'))
        self.assertLess(text.index('id="nov-3"'), text.index('id="nov-3-supplement"'))


if __name__ == '__main__':
    unittest.main()
