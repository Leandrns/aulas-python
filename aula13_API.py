'''import requests

url = "https://instagram-scraper-api2.p.rapidapi.com/v1/followers"

querystring = {"username_or_id_or_url":"leandr_nsouza"}

headers = {
	"x-rapidapi-key": "f0db65b2fdmsha2ce8efd91021c1p135b75jsn62761861eaba",
	"x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())'''

'''import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"q\"\r\n\r\nEnglish is hard, but detectably so\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": "f0db65b2fdmsha2ce8efd91021c1p135b75jsn62761861eaba",
	"x-rapidapi-host": "google-translate1.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
	"Accept-Encoding": "application/gzip"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())'''

import requests

url = "https://rocket-league1.p.rapidapi.com/stat/930226ec26174a988dff84898ee13ded/%7Bstat%7D"

headers = {
	"x-rapidapi-key": "f0db65b2fdmsha2ce8efd91021c1p135b75jsn62761861eaba",
	"x-rapidapi-host": "rocket-league1.p.rapidapi.com",
	"User-Agent": "RapidAPI Playground",
	"Accept-Encoding": "identity"
}

response = requests.get(url, headers=headers)

print(response.json())