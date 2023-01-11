import requests

url = "https://anilistmikilior1v1.p.rapidapi.com/getAccessToken"

payload = {"code":"3CREQUIRED%3E",
"clientId":"3CREQUIRED%3E",
"clientSecret":"%3CREQUIRED%3E",
"redirectUri":"%3CREQUIRED%3E"}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "d570126ac2msh96fb051648548ecp1eb7f3jsn1029200acce3",
	"X-RapidAPI-Host": "Anilistmikilior1V1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.status_code)