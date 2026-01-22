"""
Emotion Detection module using Watson NLP API.
This module provides a function to analyze emotions in a given text.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Analyze the emotion of the given text using Watson NLP Emotion Predict function.

    Args:
        text_to_analyse: The text to be analyzed for emotions.

    Returns:
        A dictionary containing emotion scores and the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, headers=headers,
                                 json=input_json, timeout=30)

        if response.status_code == 200:
            formatted_response = json.loads(response.text)

            emotions = formatted_response['emotionPredictions'][0]['emotion']
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']

            dominant_emotion = max(emotions, key=emotions.get)

            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    except (requests.exceptions.RequestException, KeyError, json.JSONDecodeError) as e:
        # 捕获所有请求相关的异常
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
