import datetime as dt
import requests
import time

def kelvin_to_celcius(kel):
    Celcius = kel - 273.15
    return Celcius

def AC_TEMP(temp_celsi,humidity):
    if temp_celsi <= 15 :
       formula = (25 + ( 1 + humidity / temp_celsi) - 8 ) 
    else :
        formula = (25 - ( 1 + humidity / temp_celsi) - 5 ) 
          
    return formula

BASE_URL ="http://api.openweathermap.org/data/2.5/weather?"
API_KEY='a2b6b6761edfaaafd64bdbdcc3925cbe'

CITY="Mumbai"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY 

current_hour = time.localtime().tm_min


while True:
    count=0
    while count<1:
       response=requests.get(url).json()
       #print(response)
       kel=response['main']['temp']
       temp_celsi= kelvin_to_celcius(kel)
       humidity= response['main']['humidity']
       ac_temp = AC_TEMP(temp_celsi,humidity)
       # print(ac_temp)
       # print(temp_celsi)
       # print(humidity)
       print(ac_temp)
       time.sleep(1800)  # Sleep for 10 minutes (600 seconds)
       count += 1
    counter=0   
    while counter<3:
        if temp_celsi > 15 :
           ac_temp +=1
        else:
           ac_temp -=1    
        counter += 1  
        print(ac_temp)
        time.sleep(480)
        
    
