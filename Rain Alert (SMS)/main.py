import requests
from twilio.rest import Client

#This variables may be saved as environment variables either in the IDE or python 'os' module
account_sid = "API_ID"
auth_token = "AUTH TOKEN"
client = Client(account_sid, auth_token)

#Weather data from 'openweathermap.org in json format
API_END = f"https://api.openweathermap.org/data/2.5/forecast?lat=10&lon=76&appid={API_ID}"
response = requests.get(API_END)
response.raise_for_status()
data = response.json()
weather_slice = data["list"][:12]
#[:12] is the data which contain favorable climate condition 'rain' to make sure that the twilio messaging app is functioning.
#Through the dictionary we can point any date and alert the weather condtion.
#Daily alerts as per the weather description can also be achieved by tagging 'datetime' module and modified script.

#Condition to avoid repititative alerts
is_rain = False
for i in weather_slice:
    condition = i["weather"][0]['id']
    if int(condition) < 700:
        is_rain = True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Subject:Rain Alert, It is going to rain today",
        from_='TWILIO ID',
        to='+TO_NUMBER')

print(message.status)
