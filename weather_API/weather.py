from operator import contains
import sys
import requests as rq


argument = sys.argv
if '-h' in argument or len(argument) == 1:
     print('''
                             _                   
                        _   | |                  
 _ _ _  _____  _____  _| |_ | |__   _____   ____ 
| | | || ___ |(____ |(_   _)|  _ \ | ___ | / ___)
| | | || ____|/ ___ |  | |_ | | | || ____|| |    
 \___/ |_____)\_____|   \__)|_| |_||_____)|_|    

following arguments are available:\n-k     provide your api key\n-l     provide the city name\n-h     print this screen                                                 
''')
elif '-k' in argument and '-l' in argument:
     key = argument[argument.index('-k')+1] #"e47efe1099567448b92eb3c9c12b5ae0"
     location = argument[argument.index('-l')+1]
     response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={location}").json()
     print(f"""
Weather: {response['weather'][0]['description']}
Temperature: from {round(response['main']['temp_min']/10)} to {round(response['main']['temp_max']/10)}
     """)
else:
     print('incorrect argument: please use -k to provide you API key and -l to provide the city name')