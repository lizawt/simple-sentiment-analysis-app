import requests

query = {'text': 'I love awolnation and would definitely recommend their ealier albums'}
response = requests.get('http://127.0.0.1:8000/sentiment_analysis/', params=query)
print(response.json())