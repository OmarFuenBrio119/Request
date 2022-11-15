from asyncio.base_subprocess import ReadSubprocessPipeProto
from email import header
from wsgiref.headers import Headers
import requests

url = 'https://rickandmortyapi.com/api/character'

payload={}
headers={}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.json())
respuesta_json = response.json()
info =(respuesta_json['info'])
personajes = (respuesta_json['results'])

#for name in respuesta_json['results']:
    #print(name['name'])
for persojane in personajes:
    print(f"El personaje {persojane['name']} esta {persojane['status']}")