import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "Virtual twilio number"
VERIFIED_NUMBER = "Verified Twilio number"

STOCK_NAME = "IBM"
COMPANY_NAME = "IBM Inc"
API_KEY_NEWS = "YOUR OWN API KEY FROM NEWSAPI"
FROM = 'date in the format YYYY-MM-MM'
STOCK_URL= 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
NEWS_URL = f'https://newsapi.org/v2/everything?q=IBM&from={FROM}&sortBy=publishedAt&apiKey={API_KEY_NEWS}'


TWILIO_SID = "ACCOUNT SID"
TWILIO_AUTH_TOKEN = "AUTH TOKEN"

#Getting Stock data

response = requests.get(STOCK_URL)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


#Calculations

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

#Symbol selection
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

#Getting news
if abs(diff_percent) > 1:
    news_response = requests.get(NEWS_URL)
    articles = news_response.json()["articles"]
    #Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]
    
   # Messaging
    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
      for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
