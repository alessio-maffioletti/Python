import sys
import requests as rq


argument = sys.argv
if len(argument) == 1:
     print('''
                             _                   
                        _   | |                  
 _ _ _  _____  _____  _| |_ | |__   _____   ____ 
| | | || ___ |(____ |(_   _)|  _ \ | ___ | / ___)
| | | || ____|/ ___ |  | |_ | | | || ____|| |    
 \___/ |_____)\_____|   \__)|_| |_||_____)|_|    

following arguments are available:\n-k     provide your api key\n-l     provide the city name\n-h     print this screen                                                 
''')
elif '-h' in argument:
     print('''following arguments are available:\n-k     provide your api key\n-l     provide the city name\n-h     print this screen
for example: write python weather.py -k soivhsodivhsdd -l zurich 
     ''')
elif '-k' in argument and '-l' in argument:
     key = argument[argument.index('-k')+1] #"e47efe1099567448b92eb3c9c12b5ae0"
     location = argument[argument.index('-l')+1]
     response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={location}").json()
     print(f"""
Weather: {response['weather'][0]['description']}
Temperature: from {round(response['main']['temp_min']- 273.15)}°C to {round(response['main']['temp_max']- 273.15)}°C
     """)
else:
     print('incorrect argument: please use -k to provide you API key and -l to provide the city name or use -h to print the help screen')