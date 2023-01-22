from news import NewsData
from stock import StockData
from message import MessagePanel

stock_result = StockData()
stock_result_value = stock_result.value()
news_data = NewsData()
message = f'Stock Alert\nIBM {stock_result_value}\n{news_data.title_1}' \
          f'\n{news_data.description_1}\nSource:{news_data.source_1}'

if stock_result.percentage > 5:
    MessagePanel.message_data(message)
else:
    print("No Alerts")

