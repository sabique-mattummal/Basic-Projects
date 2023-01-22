import requests

#Constants
API_KEY_NEWS ="Get Your Free API Key from https://newsapi.org"

# q= IBM (You can choose any company name here), from
URL= f'https://newsapi.org/v2/everything?q=IBM&from=2023-01-21&sortBy=publishedAt&apiKey={API_KEY_NEWS}'
# q= IBM (You can choose any company name here), from= desired date as per the format (YYYY-MM-DD)
#check newsapi.org for more API functions

class NewsData:
    def __init__(self):
        self.title_1 = requests.get(URL1).json()['articles'][0]['title']
        self.description_1 = requests.get(URL1).json()['articles'][0]['description']
        self.source_1 = requests.get(URL1).json()['articles'][0]['source']['name']


