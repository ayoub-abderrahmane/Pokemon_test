#
# creation le 24/01/2024
#
# 
#
#
#
import json
import urllib.request as ul
import random
import os 
#Chargement du json:
#JSON=ul.urlopen("https://pokebuildapi.fr/api/v1/pokemon")

# # Conversion du json en dictionnaire:
# data=json.loads(JSON.read())
# with open('pokedex.json', 'w', encoding='Utf-8') as f:
#    json.dump(data, f, indent=2)

#print(data[0]['name'])

class Pokedex():
    
    def __init__(self):
        
        self.data = []
        
        with open('pokedex.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        
    
    def pokedex_joueur_existe(self):
        '''Méthode qui vérifie par un bool si pokedex existe déja : 
            -Elle retourne True=existe ,false=existe pas '''

        if os.path.exists("pokedex_joueur.json"):
            return True
        else : 
            return False   

    
    def pokedex_vide(self):
        '''Méthode permettant de crée un Json vide qui sera le pokedex de départ du joueur.'''
        
        #Si le fichier n'existe pas déja
        if self.pokedex_joueur_existe() == False:
        
            #Création du pokedex du joueur 
            self.pokedex_joueur = []

            #Indice [0] = None
            with open('pokedex_joueur.json', 'a', encoding='utf-8') as f:
                self.pokedex_joueur.append(None)
                json.dump(self.pokedex_joueur, f, indent=2)
        
        
    def pokemon_aleatoire (self) :
        '''Choisi un pokemon aléatoirement dans l'api avec toutes ces infos '''
    
        #pokemon_total=898
        total_pokemon = len(self.data) - 1
        
        #Cette variable permet de choisir un pokemon à l'aide d'un indice aléatoire dans pokedex.json  
        nb_aleatoire = random.randint(1, total_pokemon)

        #Pokemon aléatoire dans le pokedex avec toutes ces infos
        self.pokemon_aleatoire_ = self.data[nb_aleatoire]
        
    
    def ajout_pokemon_rencontrer(self):
        ''' Méthode permettant d'ajouter un pokemon dans pokedex_joueur.'''
        
        #Ajout du pokemon dans le pokedex    
        with open('pokedex_joueur.json', 'r+', encoding='utf-8') as f:
            
            #Conversion du json en Dictionnaire
            self.pokedex_joueur = json.load(f)
            
            #Ajout du pokemon rencontré dans le dictionnaire pokedex_joueur
            self.pokedex_joueur.append(self.pokemon_aleatoire_)
            f.seek(0)

            #Conversion du dictionnaire en Json
            json.dump(self.pokedex_joueur, f, indent=2)
        
        
        # def suppression_pokedex_joueur(self):
        #     if
            
    
pokedex=Pokedex()

pokedex.pokedex_vide()
pokedex.pokemon_aleatoire() 
pokedex.ajout_pokemon_rencontrer()
