"""
Server file which has route functions

"""
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detection",template_folder='templates')

@app.route("/emotionDetector")
def emotion_detect():
    '''
    Detect emotions
    '''
    texti=request.args.get('textToAnalyze')
    resp=emotion_detector(texti)
    if resp['dominant_emotion'] is None:
        mod_res="Invalid text! Please try again!."
    else:
        mod_res=f"For the given statement, the system response is 'anger': {resp['anger']},"
        mod_res+=f"'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']} and"
        mod_res+=f"'sadness': {resp['sadness']}. The dominant emotion is"
        mod_res+=f" {resp['dominant_emotion']}."
    # mod_res="Hello"
    return mod_res

@app.route("/")
def render_index_page():
    '''
    renders Index Page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
