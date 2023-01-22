import requests
import datetime

class StockData:
    def __init__(self):
      #Dates are modifies as per last two days from datetime, make sure the market dates and stocks are quoted on the dates from json data
        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=2)
        date_yesterday = yesterday.strftime('%Y-%m-%d')
        self.day_before_yesterday = today - datetime.timedelta(days=4)
        dby_date = self.day_before_yesterday.strftime('%Y-%m-%d')
        
        URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
        
        #symbol=IBM (You ca put any company name
        
        yesterday_closing_value = float(requests.get(URL).json()['Time Series (Daily)'][f'{date_yesterday}']['4. close'])
        self.day_before_yesterday_closing_value = float(requests.get(URL).json()['Time Series (Daily)'][f'{dby_date}']['4. close'])
        self.differnce = yesterday_closing_value - self.day_before_yesterday_closing_value
        self.percentage = round(self.differnce / self.day_before_yesterday_closing_value * 100, 2)
        
    #Function returning calcuated values for message

    def value(self):
            pointer = ""
            if self.differnce < 0:
                pointer = '🔻'
            if self.differnce > 0 :
                pointer = '🔺'    

            return f'{pointer}{self.percentage}%'
