import requests, json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = Input, headers=Headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        result = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }
        return result
    result = {
                'anger': formatted_response["emotionPredictions"][0]["emotion"]["anger"],
                'disgust': formatted_response["emotionPredictions"][0]["emotion"]['disgust'],
                'fear': formatted_response["emotionPredictions"][0]["emotion"]['fear'],
                'joy': formatted_response["emotionPredictions"][0]["emotion"]['joy'],
                'sadness': formatted_response["emotionPredictions"][0]["emotion"]['sadness'],
                'dominant_emotion': next((key for key, value in formatted_response["emotionPredictions"][0]["emotion"].items() if value == max(formatted_response["emotionPredictions"][0]["emotion"].values())), None)   
                }
    return result