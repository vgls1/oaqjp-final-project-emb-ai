"""
Flask application for detecting emotions from text input.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector  # Ensure this module is available

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector_route():
    """
    Analyze the provided text and return detected emotions.
    """
    text_to_analyze = request.form.get('text', '')

    if not text_to_analyze.strip():
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    response = (
        f"For the given statement, the system response is: "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}."
        f" The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')