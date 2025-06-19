"""Server module for emotion detection web interface"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the index HTML page"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Process POST request with text input,
    run emotion detection, and return results.
    """
    text_to_analyze = request.form["textToAnalyze"]
    result = emotion_detector(text_to_analyze)

    if result:
        dominant_emotion = result["dominant_emotion"]
        return render_template(
            "index.html",
            emotion_result=(
                f"For the given statement, the system response is "
                f"anger: {result['anger']}, "
                f"disgust: {result['disgust']}, "
                f"fear: {result['fear']}, "
                f"joy: {result['joy']}, "
                f"sadness: {result['sadness']}. "
                f"The dominant emotion is {dominant_emotion}."
            )
        )
    return render_template(
        "index.html",
        emotion_result="Invalid input or API error. Please try again."
    )

if __name__ == "__main__":
    app.run(debug=True)
