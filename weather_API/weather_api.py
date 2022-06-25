import requests
import json
import sys

argument = sys.argv
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
headers = {
	"X-RapidAPI-Key": "534eb5ffb9msh0a0b16f230fd35dp1923b1jsn4d148afab419",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
if len(argument) == 1:
    print("""
                                888    888                                               d8b 
                                888    888                                               Y8P 
                                888    888                                                   
888  888  888  .d88b.   8888b.  888888 88888b.   .d88b.  888d888        8888b.  88888b.  888 
888  888  888 d8P  Y8b     "88b 888    888 "88b d8P  Y8b 888P"             "88b 888 "88b 888 
888  888  888 88888888 .d888888 888    888  888 88888888 888           .d888888 888  888 888 
Y88b 888 d88P Y8b.     888  888 Y88b.  888  888 Y8b.     888           888  888 888 d88P 888 
 "Y8888888P"   "Y8888  "Y888888  "Y888 888  888  "Y8888  888           "Y888888 88888P"  888 
                                                                                888          
                                                                                888          
                                                                                888          
Welcome to weather API
To get started type --help as argument to print the help screen:
$ python weather_api.py --help
    """)
elif '--help' in argument:
    print('''following arguments are available:\n-city        provide the city name\n-forecast    number of days to forecast(0-2). Will return current weather if not providet \n--help       print this screen
for example: 
    $ python weather_api.py -city berlin -forecast 2 
    ''')
elif '-city' in argument:
    city = argument[argument.index('-city')+1]
    querystring = {"q":{city},"days":"3"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    if '-forecast' in argument:
        day = int(argument[argument.index('-forecast')+1])
        print(f"""
Condition: {response["forecast"]["forecastday"][day]["day"]["condition"]["text"]}
Temperature: from {response["forecast"]["forecastday"][day]["day"]["mintemp_c"]}°C to {response["forecast"]["forecastday"][day]["day"]["maxtemp_c"]}°C
Max Wind: {response["forecast"]["forecastday"][day]["day"]["mintemp_c"]}kph
Precipitation: {response["forecast"]["forecastday"][day]["day"]["totalprecip_mm"]}mm
Chance of Rain: {response["forecast"]["forecastday"][day]["day"]["daily_chance_of_rain"]}%
        """)
    else:
        print(f"""
Condition: {response["current"]["condition"]["text"]}
Temperature: {response["current"]["temp_c"]}°C
Wind: {response["current"]["wind_kph"]}kph
Precipitation: {response["current"]["precip_mm"]}mm
        """)
else:
    print('invalid argument:\n--help for help')