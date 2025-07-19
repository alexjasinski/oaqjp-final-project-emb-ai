"""Emotion detection module using Watson NLP API."""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyze the emotions in the given text using Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary with emotion scores and the dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=10  # timeout in seconds
    )

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant
    }
