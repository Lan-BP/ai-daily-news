import unittest
from unittest.mock import patch

import feed_v5


class FeedLinkTests(unittest.TestCase):
    def test_relative_article_links_are_resolved_before_ranking(self):
        atom = '''<feed xmlns="http://www.w3.org/2005/Atom">
          <title>Sakana Blog</title>
          <entry><title>Sakana API Platform</title>
            <id>/api-platform-earlyaccess</id>
            <link href="/api-platform-earlyaccess"/>
            <published>2026-10-28T00:00:00+09:00</published>
          </entry>
        </feed>'''

        class Response:
            text = atom

            def raise_for_status(self):
                pass

        with patch.object(feed_v5.httpx, 'Client') as client, \
                patch.object(feed_v5, 'is_in_window', return_value=True), \
                patch.object(feed_v5, 'calculate_priority_v2', return_value=30):
            client.return_value.get.return_value = Response()
            articles, error = feed_v5.fetch_source(
                'Sakana Blog', 'https://sakana.ai/feed.xml', max_retries=1
            )

        self.assertIsNone(error)
        self.assertEqual(len(articles), 1)
        self.assertEqual(
            articles[0]['link'], 'https://sakana.ai/api-platform-earlyaccess'
        )

    def test_absolute_links_keep_their_original_destination(self):
        atom = '''<feed xmlns="http://www.w3.org/2005/Atom">
          <entry><title>Original announcement</title>
          <link href="https://publisher.example/news/launch"/></entry>
        </feed>'''
        with patch.object(feed_v5.httpx, 'Client') as client, \
                patch.object(feed_v5, 'is_in_window', return_value=True), \
                patch.object(feed_v5, 'calculate_priority_v2', return_value=30):
            client.return_value.get.return_value.text = atom
            articles, error = feed_v5.fetch_source(
                'Example', 'https://feeds.example/feed.xml', max_retries=1
            )
        self.assertIsNone(error)
        self.assertEqual(articles[0]['link'], 'https://publisher.example/news/launch')

    def test_missing_article_link_does_not_become_the_feed_url(self):
        with patch.object(feed_v5.httpx, 'Client') as client, \
                patch.object(feed_v5, 'is_in_window', return_value=True), \
                patch.object(feed_v5, 'calculate_priority_v2', return_value=30):
            client.return_value.get.return_value.text = (
                '<rss><channel><item><title>Article without link</title>'
                '</item></channel></rss>'
            )
            articles, error = feed_v5.fetch_source(
                'Example', 'https://feeds.example/feed.xml', max_retries=1
            )
        self.assertIsNone(error)
        self.assertEqual(articles[0]['link'], '')


if __name__ == '__main__':
    unittest.main()
