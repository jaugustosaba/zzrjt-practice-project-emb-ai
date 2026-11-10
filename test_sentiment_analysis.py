import unittest
from SentimentAnalysis import sentiment_analyzer


class TestSentimentAnalyser(unittest.TestCase):
    def test_sentiment_analyser(self):
        self.assertEqual(sentiment_analyzer('I love working with Python')['label'], 'SENT_POSITIVE')
        self.assertEqual(sentiment_analyzer('I hate working with Python')['label'], 'SENT_NEGATIVE')
        self.assertEqual(sentiment_analyzer('I am neutral on Python')['label'], 'SENT_NEUTRAL')


if __name__ == '__main__':
    unittest.main()