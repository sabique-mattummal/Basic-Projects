#imports

from datetime import datetime
import pandas
import random
from smtplib import SMTP

#user_providing_data

SELF_EMAIL= 'email'
SELF_PASSWORD = 'password'
#this passowrd is specially provided by smtp permission mail provider

#date check

today = datetime.now()
today_tuple = (today.month, today.day)

#import birthday data from csv

data = pandas.read_csv('Birthdays.csv')

#creation of a dictionary with a tuple to compare the values as per the need

birthdays_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}

#condition check
if today_tuple in birthdays_dict:
    #name of the person
    birthdays_person = birthdays_dict[today_tuple]
    #selecting a random letter by the random method
    file_path = f'sample_letters/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter:
        contents = letter.read()
        #change the name of the person 
        contents = contents.replace('[NAME]', birthdays_person['name'])
        
    #mail despatch
    with SMTP('smtp.gamail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,msg=f"Subject:Birthday Greetings\n\n{contents}")
        


