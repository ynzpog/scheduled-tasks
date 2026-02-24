import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
LAT = 14.848560
LONG = 120.982040
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

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
client = Client(account_sid, auth_token)
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639399101416",
    )
    print(message.status)
else:    
    message = client.messages.create(
        body="No rain🌞🌞",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639399101416",
    )
    print(message.status)
