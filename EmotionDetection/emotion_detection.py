import requests
import json


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

    response = requests.post(url, headers=headers, json=input_json)

    # 将响应文本转换为字典
    formatted_response = json.loads(response.text)

    # 提取情绪分数
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # 找到得分最高的情绪作为主导情绪
    dominant_emotion = max(emotions, key=emotions.get)

    # 构建并返回所需的格式
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
