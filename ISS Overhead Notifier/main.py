#imports

import requests
from datetime import datetime
import smtplib
import time

#User data

MY_EMAIL = "email"
MY_PASSWORD = "password"
MY_LAT = 'my_lat'
MY_LONG = 'my_long'

#Functions

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    response_time = requests.get(f'https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0').json()
    sunrise = int(response_time['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(response_time['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#Condition

while True:
    time.sleep(10)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.google.com', port=587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:ISS Overhead notification\n\nThe ISS is above you in the sky."
        )


