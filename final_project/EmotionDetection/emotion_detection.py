"""
Function to detect emotions using the Watson NLP library
"""

import requests, json

def emotion_detector(text_to_analyse):
    """
    This function enables communication with the Watson API for emotion detection
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_data.get('anger', 0)
    disgust_score = emotion_data.get('disgust', 0)
    fear_score = emotion_data.get('fear', 0)
    joy_score = emotion_data.get('joy', 0)
    sadness_score = emotion_data.get('sadness', 0)

    emotions_only = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    dominant_emotion = max(emotions_only, key=emotions_only.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
