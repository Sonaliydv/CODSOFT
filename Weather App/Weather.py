import requests
from tkinter import *

api = "http://api.weatherapi.com/v1/current.json"
api_key = "d9e8f15bb7e844998a925913231808"


def weather_report():
    user_input = user_entry.get()

    parameters = {
        "key": api_key,
        "q": user_input,
        "aqi": "no"
    }

    response = requests.get(url=api, params=parameters)

    weather_data = response.json()
    # print(weather_data)

    try:
        place_name = weather_data['location']['name']
        region_name = weather_data['location']['region']
        country_name = weather_data['location']['country']
        date = weather_data['location']['localtime'].split(' ')[0]
        time = weather_data['location']['localtime'].split(' ')[1]
        temperature = weather_data['current']['temp_c']
        temperature_fl = weather_data['current']['feelslike_c']
        condition = weather_data['current']['condition']['text']
        wind_speed = weather_data['current']['wind_mph']
        humidity = weather_data['current']['humidity']
        cloud = weather_data['current']['cloud']
        weather = f"Location: {place_name}, {region_name}, {country_name}\nDate: {date}\nTime: {time}\nTemperature: {temperature}°C\nReal Feel: {temperature_fl}°C\nCondition: {condition}\nWind Speed: {wind_speed}mph\nHumidity: {humidity}\nCloud: {cloud}"
    except KeyError:
        weather = "Error: No matching location found."
    text_field.delete("1.0", "end")
    text_field.insert(INSERT, weather)


window = Tk()
window.geometry("350x300")
window.title("Weather Reports")
window.configure(bg='#856ff8')

Label(text="Enter Location:", bg='#856ff8', font=("Times", 14, "bold")).pack(pady=5)
user_entry = Entry()
user_entry.pack()
Button(text="Get Weather Reports", command=weather_report, bg="light cyan").pack(pady=10)

text_field = Text(width=40, height=10, pady=10, bg="light yellow")
text_field.pack()

window.mainloop()
