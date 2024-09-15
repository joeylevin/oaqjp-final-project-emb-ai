import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    else:
        scores = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = scores['anger']
        disgust_score = scores['disgust']
        fear_score = scores['fear']
        joy_score = scores['joy']
        sadness_score = scores['sadness']
        dominant_emotion = ''
        max_score = 0
        for emotion in scores: 
            if scores[emotion] > max_score:
                max_score = scores[emotion]
                dominant_emotion = emotion
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
