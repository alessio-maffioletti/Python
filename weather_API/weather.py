import requests as rq

print('''
                             _                   
                        _   | |                  
 _ _ _  _____  _____  _| |_ | |__   _____   ____ 
| | | || ___ |(____ |(_   _)|  _ \ | ___ | / ___)
| | | || ____|/ ___ |  | |_ | | | || ____|| |    
 \___/ |_____)\_____|   \__)|_| |_||_____)|_|    
                                                 
''')

key = "{YOUR KEY}"
location = input('city name: ')

response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={location}").json()
print(f"""
Weather: {response['weather'][0]['description']}
Temperature: from {round(response['main']['temp_min']/10)} to {round(response['main']['temp_max']/10)}
""")
