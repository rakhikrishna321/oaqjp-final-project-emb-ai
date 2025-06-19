import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/recognize"
    params = {"text": text_to_analyze}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    result = response.json()

    if "emotionPredictions" not in result or not result["emotionPredictions"]:
        return None

    emotions = result["emotionPredictions"][0]["emotion"]
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return a dictionary with all emotions and dominant emotion
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
