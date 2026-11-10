'''
sentiment_analysis
'''
import json
import requests


def sentiment_analyzer(text_to_analyse):
    '''sentiment_analyzer'''
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/' +
        'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict')
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock",
    }
    data = {
        "raw_document": { "text": text_to_analyse },
    }
    response = requests.post(url, headers=headers, json=data, timeout=30)
    label = None
    score = None
    if response.status_code == 200:
        out = json.loads(response.text)
        label = out['documentSentiment']['label']
        score = out['documentSentiment']['score']
    return  { 'label': label, 'score': score }
