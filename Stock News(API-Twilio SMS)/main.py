from news import NewsData
from stock import StockData
from message import MessagePanel
from twilio.rest import Client

#Twilio Constants
Account_sid = 'Your Twilio account sid'
Auth_token = 'Your auth token)
My_numb = 'Virual Twilio Number
To_numb = 'To_num"


stock_result = StockData()
stock_result_value = stock_result.value()
news_data = NewsData()
message = f'Stock Alert\nIBM {stock_result_value}\n{news_data.title_1}' \
          f'\n{news_data.description_1}\nSource:{news_data.source_1}'

if stock_result.percentage > 5:
          client = Client(Account_sid, Auth_token)
          message = client.messages.create(body=message, from=My_num, to=To_num) 
 
else:
    print("No Alerts")

