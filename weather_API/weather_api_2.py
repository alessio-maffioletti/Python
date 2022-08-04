import argparse as arg
import requests as rq
import sys

def main():
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    headers = {
        "X-RapidAPI-Key": "534eb5ffb9msh0a0b16f230fd35dp1923b1jsn4d148afab419",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    parser = arg.ArgumentParser()
    parser.add_argument('-help', help='foo help')
    parser.add_argument('city')
    parser.add_argument('-forecast', type=int)
    args = parser.parse_args()
    city = args.city
    querystring = {"q":{city},"days":"3"}
    request = rq.request("GET", url, headers=headers, params=querystring)
    response = request.json()
    assert request.status_code == 200, 'please provide a valid city'
    print(f"""
Location: {response["location"]["name"]} in {response["location"]["country"]}
Condition: {response["current"]["condition"]["text"]}
Temperature: {response["current"]["temp_c"]}°C
Wind: {response["current"]["wind_kph"]}kph
Precipitation: {response["current"]["precip_mm"]}mm
    """)

if __name__ == "__main__":
    sys.exit(main())