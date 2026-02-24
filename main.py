import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("a3df354b953bb334ac2c05d15a62f6ba")
LAT = 14.848560
LONG = 120.982040
account_sid = os.environ.get("AC1e0cdc4e0e6725d66e2fbd2ab552b5fc")
auth_token = os.environ.get("cb1bb7cb5e50b1397d6555e78be865f5")

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt" : 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639399101416",
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="No rain🌞🌞",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639399101416",
    )
    print(message.status)
