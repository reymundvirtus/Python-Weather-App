from tkinter import *
import requests
from datetime import datetime, time
from time import strftime
from PIL import Image, ImageTk
import urllib
from urllib.request import urlopen

city = "Canaman"
api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=7bd6b4d0243c4d2c4f341aec450f7d88"
json_data = requests.get(api).json()
description = json_data["weather"][0]["description"].title()
temperature = int(json_data["main"]["temp"] - 273.15)

def getWeather():
    #api = "http://api.weatherstack.com/current?access_key=0deca4e241615187becca38d81f81ed4&query=" + city
    #main = json_data["weather"][0]["main"]
    global city, api, description, temperature
    city = "Canaman"
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=7bd6b4d0243c4d2c4f341aec450f7d88"
    json_data = requests.get(api).json()
    description = json_data["weather"][0]["description"].title()
    temperature = int(json_data["main"]["temp"] - 273.15)
    #icon = ImageTk(json_data["weather"]["icon"])
    #minimum_temperature = int(json_data["temperature"]["temp_min"]) #  - 273.15
    #maximum_temperature = int(json_data["temperature"]["temp_max"])
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    #sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - 21600))
    #sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - 21600))
    
    final_info = city + "  " + str(temperature) + "°C  |  " + str(temperature * 9 / 5 + 32) + "°F" + "\n" + str(description)
    #final_data = "\n" + "Max Temp: " + str(maximum_temperature) + "°C" + "\n" + "Min Temp: " + str(minimum_temperature) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind)
    
    label1.config(text = final_info)
    label1.after(60000, getWeather)
    #label2.config(text = final_data)


day = strftime("%A")
hour = strftime("%I:%M %p")
def time():
    global hour, day
    day = strftime("%A")
    hour = strftime("%I:%M %p")
    current_time = strftime("%Y/%m/%d\n"+ day[0:3] + ", " + hour)
    label.config(text = current_time)
    label.after(1000, time)


def greetings():
    if hour == strftime("%I:%M AM"):
        if hour >= strftime("12:00") and hour <= strftime("12:59"):
            message = morning
            greet.config(text = message)
        elif hour >= strftime("01:00") and hour <= strftime("11:59"):
            message = morning
            greet.config(text = message)
    elif hour == strftime("%I:%M PM"):
        if hour >= strftime("12:00") and hour <= strftime("12:59"):
            message = afternoon
            greet.config(text = message)
        elif hour >= strftime("01:00") and hour <= strftime("05:59"):
            message = afternoon
            greet.config(text = message)
        elif hour >= strftime("06:00") and hour <= strftime("09:59"):
            message = evening
            greet.config(text = message)
        elif hour > strftime("10:00") and hour < strftime("12:00"):
            message = night
            greet.config(text = message)

    greet.after(1000, greetings)


def weather_images():    
    if description == "Broken Clouds" or description == "Overcast Clouds":
        img = broken_overcast_clouds
        weather_img.config(image = img)
    elif description == "Few Clouds" or description == "Scattered Clouds":
        img = few_scattered_clouds
        weather_img.config(image = img)
    elif description == "Light Rain" or description == "Moderate Rain":
        img = light_moderate_rain
        weather_img.config(image = img)
    elif description == "Clear Sky":
        img = clear_sky
        weather_img.config(image = img)
    elif description == "Heavy Intensity Rain" or description == "Very Heavy Rain" or description == "extreme rain":
        img = heavy_rains
        weather_img.config(image = img)
    elif description == "Rain":
        img = rain
        weather_img.config(image = img)
    elif description == "Thunderstorm With Light Rain" or description == "Thunderstorm With Rain" or description == "Thunderstorm With Heavy Rain" or description == "Light Thunderstorm" or description == "Thunderstorm":
        img = thunder_storm
        weather_img.config(image = img)
    else:
        img = default_img
        weather_img.config(image = img)

    weather_img.after(1000, weather_images)


def day_or_night():
    if hour == strftime("%I:%M PM"):
        if hour >= strftime("12:00") and hour <= strftime("12:59"):
            day = sun
            day_img.config(image = day)
        elif hour >= strftime("01:00") and hour <= strftime("05:59"):
            day = sun
            day_img.config(image = day)
        elif hour >= strftime("06:00") and hour <= strftime("11:59"):
            day = moon
            day_img.config(image = day)
    elif hour == strftime("%I:%M AM"):
        if hour >= strftime("12:00") and hour <= strftime("12:59"):
            day = moon
            day_img.config(image = day)
        elif hour >= strftime("01:00") and hour <= strftime("03:59"):
            day = moon
            day_img.config(image = day)
        elif hour >= strftime("04:00") and hour <= strftime("11:59"):
            day = sun
            day_img.config(image = day)

    day_img.after(1000, day_or_night)


def test_connection():
    try:
        urlopen("https://www.google.com")
        return True
    except urllib.error.URLError as Error:
        getWeather()

    test_label.after(1000, test_connection)


canvas = Tk()
app_width = 450
app_height = 330
screen_width = canvas.winfo_screenwidth()
screen_height = canvas.winfo_screenheight()
x = (screen_width / 6.5) - (app_width / 2)
y = (screen_height / 4) - (app_height / 2)
canvas.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
canvas.title("Weather Widget")
canvas.iconbitmap("icons/favicon.ico")
canvas.config(bg = '#f2f7f4')
canvas.wm_attributes('-transparentcolor','#f2f7f4')

f = ("Cambria", 20) # font family is "tahoma", font size "15", font type "bold"
time_font = ("Death Hector", 20)
weather_font = ("Cambria", 25, "bold")
greetSize = ("Constantia", 16)

'''textField = Entry(canvas, font = t)
textField.pack(pady = 20)
textField.focus() # setting textfield to focus to type immedietly
textField.bind("<Return>", getWeather)'''

# day or night message
sun = PhotoImage(file = "icons\sunny.png")
moon = PhotoImage(file = "icons\moon.png")

# Day or Night
day_img = Label(canvas, bg = "#f2f7f4")
day_img.pack()
day_or_night()
    
# for time display
label = Label(canvas, font = time_font, fg = "white", bg = "#f2f7f4")
label.pack(pady = 10)
time()

# greetings text
morning = "Good Morning! | おはようございます"
afternoon = "Good Afternoon! | こんにちは"
evening = "Good Evening! | こんばんは"
night = "Good Night! | おやすみなさい"

# for greetings
greet = Label(canvas, font = greetSize, fg = "white", bg = "#f2f7f4")
greet.pack()
greetings()

# for city & weather display
label1 = Label(canvas, font = weather_font, fg = "white", bg = "#f2f7f4")
label1.pack(pady = 5)
getWeather()

# weather images
broken_overcast_clouds = PhotoImage(file = "icons\clouds.png")
few_scattered_clouds = PhotoImage(file = "icons\partly-cloud.png")
light_moderate_rain = PhotoImage(file = "icons\light-rain.png")
clear_sky = PhotoImage(file = "icons\sunny.png")
heavy_rains = PhotoImage(file = "icons\heavy-rain.png")
rain = PhotoImage(file = "icons\sunny-rain.png")
thunder_storm = PhotoImage(file = "icons\\thunder-cloud.png")
default_img = PhotoImage(file = "icons\partly-cloud.png")

# for weather images
weather_img = Label(canvas, bg = "#f2f7f4")
weather_img.pack()
weather_images()

# testing if there is an internet connection
test_label = Label(canvas, bg = "#f2f7f4")
test_label.pack()
test_connection()

'''label2 = Label(canvas, font = f, fg = "white", bg = "#f2f7f4")
label2.pack()'''


canvas.overrideredirect(1)
canvas.mainloop()