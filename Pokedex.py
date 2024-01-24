#
# creation le 24/01/2024
#
# 
#
#
#
import json
import urllib.request as ul

#Chargement du json
JSON=ul.urlopen("https://pokebuildapi.fr/api/v1/pokemon")

#Conversion du json en dictionnaire
data=json.loads(JSON.read())

print (data[0])