import requests

url = "https://currencyconverter.p.rapidapi.com/"

querystring = {"from_amount":"1","from":"USD","to":"SEK"}

headers = {
	"X-RapidAPI-Key": "e9a2180997msh492b13cd5c10dc0p123a6fjsn0a55c2d8b7ca",
	"X-RapidAPI-Host": "currencyconverter.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())