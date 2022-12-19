import http.client

conn = http.client.HTTPSConnection("password-server-api.herokuapp.com")

headers = {
    'X-RapidAPI-Key': "2108f80b77mshaf0336394348824p1db97ajsn3cb95bcc0723",
    'X-RapidAPI-Host': "password-generator8.p.rapidapi.com"
    }

conn.request("GET", "/?length=8&uppercases=3&lowercases=3&digits=3&specials=3", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


'''

import requests

url = "http://127.0.0.1:8000/"

querystring = {"length":"30","uppercases":"5","lowercases":"5","digits":"5","specials":"5"}

headers = {
	"X-RapidAPI-Key": "2108f80b77mshaf0336394348824p1db97ajsn3cb95bcc0723",
	"X-RapidAPI-Host": "password-generator8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

'''