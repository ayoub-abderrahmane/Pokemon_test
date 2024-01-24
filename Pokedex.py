#
# creation le 24/01/2024
#
# 
#
#
#
import json
import urllib.request as ul

#Chargement du json:
#JSON=ul.urlopen("https://pokebuildapi.fr/api/v1/pokemon")

#Conversion du json en dictionnaire:
#data=json.loads(JSON.read())
#with open('pokedex.json', 'w', encoding='utf-8') as f:
#    json.dump(data, f, indent=2)
#print(data[0]['name'])




class Pokedex():
    
    def __init__(self,):
        self.data = []
        with open('pokedex.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        

    def affichage(self):
        print(self.data)


pokedex=Pokedex()

