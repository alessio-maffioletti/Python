import requests

url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"
text = 'ich bin ein lieber roboter'

payload = f"voice_code=de-CH-1&text={text}&speed=1.00&pitch=1.00&output_type=audio_url"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "534eb5ffb9msh0a0b16f230fd35dp1923b1jsn4d148afab419",
	"X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json())