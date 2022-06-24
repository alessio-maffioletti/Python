import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"73354e968d6e461ab437e1af9f48cd66"}

payload = "f=8khz_8bit_mono&c=mp3&r=0&hl=en-us&src=Hello%2C%20world!"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "534eb5ffb9msh0a0b16f230fd35dp1923b1jsn4d148afab419",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.json())