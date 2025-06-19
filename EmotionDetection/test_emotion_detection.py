import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_joy(self):
        result = emotion_detector("I am so happy and joyful today!")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_anger(self):
        result = emotion_detector("I am very angry and frustrated.")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_sadness(self):
        result = emotion_detector("I feel sad and down.")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_emotion_fear(self):
        result = emotion_detector("I'm scared and fearful of the dark.")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_emotion_disgust(self):
        result = emotion_detector("I feel disgusted and sickened by this.")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "disgust")

if __name__ == "__main__":
    unittest.main()
