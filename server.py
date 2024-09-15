''' Executing this function initiates the application of Emotion
    Detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
    runs Emotion Detection on it using emotion_detector()
    function. 
    '''
    # Retrieve the text from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    # Return a formatted string
    return f"For the given statement, the system response is 'anger': {anger_score}, \
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. \
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
