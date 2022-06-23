import requests as rq

key = "e47efe1099567448b92eb3c9c12b5ae0"
location = input('city name: ')

response = rq.get(f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={location}").json()
print(f"""
Weather: {response['weather'][0]['description']}
Temperature: from {round(response['main']['temp_min']/10)} to {round(response['main']['temp_max']/10)}
""")
#print('Weather:', response['weather'][0]['description'])
#print('Temperature:', 'from', round(response['main']['temp_min']/10), 'to', round(response['main']['temp_max']/10))