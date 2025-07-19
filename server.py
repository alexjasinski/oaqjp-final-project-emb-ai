"""
Flask server for emotion detection web application.
"""

from flask import Flask, render_template, request, jsonify

try:
    from EmotionDetection import emotion_detector
except ImportError:
    # Provide a fallback mock function
    def emotion_detector(text):
        return {
            "anger": 0.1,
            "disgust": 0.0,
            "fear": 0.05,
            "joy": 0.2,
            "sadness": 0.15,
            "dominant_emotion": "joy"
        }

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle emotion detection requests via POST.
    """
    text_to_analyze = request.form.get("text", "")
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

cd     result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text or emotion analysis failed"}), 400

    # Return a JSON response instead of plain text
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000)