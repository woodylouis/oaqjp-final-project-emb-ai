import requests
import json


def emotion_detector(text_to_analyse):
    """
    Analyze the emotion of the given text using Watson NLP Emotion Predict function.

    Args:
        text_to_analyse: The text to be analyzed for emotions.

    Returns:
        The text attribute of the response object from the Emotion Detection function.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=input_json)

    return response.text
