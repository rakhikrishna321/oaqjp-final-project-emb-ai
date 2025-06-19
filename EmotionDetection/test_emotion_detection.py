from EmotionDetection import emotion_detection

def test_emotion_detector(): 
    assert(emotion_detection.emotion_detector("I am glad this happened")['dominant_emotion'] == 'joy')
    assert(emotion_detection.emotion_detector("I am really mad about this")['dominant_emotion'] == 'anger')
    assert(emotion_detection.emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'] == 'disgust')
    assert(emotion_detection.emotion_detector("I am so sad about this")['dominant_emotion'] == 'sadness')
    assert(emotion_detection.emotion_detector("I am really afraid that this will happen")['dominant_emotion'] == 'fear')
