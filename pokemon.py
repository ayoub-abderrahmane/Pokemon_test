import json
from Pokedex import Pokedex

class Pokemon():
    
    def __init__(self,data: dict):
        # super().__init__()        
        # super().ajout_pokemon_rencontrer() 
        

        self.pokedex_joueur = []
        with open('pokedex_joueur.son', 'r', encoding='utf-8') as f:
            self.pokedex_joueur = json.load(f)
       
               

    def pokemon1(self):
        '''Méthode qui donne les infos principal du pokemon_du_joueur'''
        
        self.nom_pokemon1 = self.pokedex_joueur[1]['name']
        self.image_pokemon1 = self.pokedex_joueur[1]['image']
        self.pv_pokemon1 = self.pokedex_joueur[1]['stats']['HP']
        self.attaque_pokemon1 = self.pokedex_joueur[1]['stats']['attack']
        self.defence_pokemon1 = self.pokedex_joueur[1]['stats']['defense']
        self.type_pokemon1 = self.pokedex_joueur[1]['apiTypes'][0]['name']
       
    def pokemon2(self):
        '''Méthode qui donne les infos principal de l'adversaire:
            Si nombre total de pokemon dans le pokedex est égale à 1:
                -On ajoute un pokemon dans le pokedex
                    
            Sinon : 
                -Le dernier pokemon du pokedex devient l'adversaire 
        '''
        
        while True  :    
           
            #Nombre total de pokemon dans pokedex
            Total_pokedex = len(self.pokedex_joueur) - 1
            

            if Total_pokedex == 1:
                #on ajoute un pokemon dans le pokedex
                super().ajout_pokemon_rencontrer()
            
            else:
                
                self.nom_pokemon2 = self.pokedex_joueur[Total_pokedex]['name']
                self.image_pokemon2 = self.pokedex_joueur[Total_pokedex]['image']
                self.pv_pokemon2 = self.pokedex_joueur[Total_pokedex]['stats']['HP']
                self.attaque_pokemon2 = self.pokedex_joueur[Total_pokedex]['stats']['attack']
                self.type_pokemon2 = self.pokedex_joueur[Total_pokedex]['apiTypes'][0]['name']
                self.defence_pokemon2 = self.pokedex_joueur[Total_pokedex]['stats']['defense']
                break
    
if __name__ == "__main__" :       
    Pokemon() 
# pokemon.pokemon2()

    



