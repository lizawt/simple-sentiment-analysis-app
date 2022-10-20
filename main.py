from transformers import pipeline
from fastapi import FastAPI

# Instantiate a pipepline object with the task and model passed as params
nlp = pipeline(task="sentiment-analysis",
model = "nlptown/bert-base-multilingual-uncased-sentiment")

app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'This is the sentiment analysis app'}

@app.get('/sentiment_analysis/')
async def query_sentiment_analysys(text: str):
    return analyse_sentiment(text)

def analyse_sentiment(text):
    """Get and process result"""

    result = nlp(text)

    sent = ''
    if (result[0]['label'] == '1 star'):
        sent = 'very negative'
    elif (result[0]['label'] == '2 star'):
        sent = 'negative'
    elif (result[0]['label'] == '3 stars'):
        sent = 'neutral'
    elif (result[0]['label'] == '4 stars'):
        sent = 'positive'
    else:
        sent = 'very positive'

    prob = result[0]['score']

    # Format and return results
    return {'sentiment': sent, 'probability': prob}

