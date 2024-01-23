import requests
import json
def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        mydict={
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        response=json.loads(response.text)
        
        emotions=response["emotionPredictions"][0]["emotion"]
        emo_arr=[]
        emo_arr.append(emotions["anger"])
        emo_arr.append(emotions["disgust"])
        emo_arr.append(emotions["fear"])
        emo_arr.append(emotions["joy"])
        emo_arr.append(emotions["sadness"])
        dom_emo=emo_arr.index(max(emo_arr))
        if dom_emo==0:
            dom_emo="anger"
        elif dom_emo==1:
            dom_emo="disgust"
        elif dom_emo==2:
            dom_emo="fear"
        elif dom_emo==3:
            dom_emo="joy"
        else:
            dom_emo="sadness"
        mydict=  {
    'anger': emo_arr[0],
    'disgust': emo_arr[1],
    'fear': emo_arr[2],
    'joy': emo_arr[3],
    'sadness': emo_arr[4],
    'dominant_emotion': dom_emo
    }
    return mydict
