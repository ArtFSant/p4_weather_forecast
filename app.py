from flask import Flask, render_template, url_for
#from flask_session import Session
import requests
import datetime as dt

app = Flask(__name__)
#app.secret_key = 'secret_key_exemple_123'

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

API_LINK = 'https://api.open-meteo.com/v1/forecast'

forecast_parameters = {
    'latitude': -8.2877,
    'longitude': -35.0292,
    'daily': 'weather_code',
    'hourly': 'temperature_2m',
    'timezone': 'auto'
}

date_now = dt.datetime.now()
print(f'{date_now}')
hour_now = date_now.hour
print(hour_now)

weather_forecast = requests.get(API_LINK, params=forecast_parameters)
weather_data = weather_forecast.json()
w_time = weather_data['hourly']['temperature_2m'][hour_now]
w_code = weather_data['daily']['weather_code'][0]

if weather_forecast.status_code == 200:
    print('Sucesso no Request')
    print(weather_data)
else:
    print(f'Erro: {weather_forecast.status_code}')

@app.route('/')
def index():
    return render_template('index.html', w_time=w_time, w_code=w_code)

if __name__ == '__main__':
    app.run(debug=True)