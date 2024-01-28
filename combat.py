import random
from pokemon import Pokemon

class Combat(Pokemon):

    def __init__(self):
        super().__init__()
        super().pokemon1()
        super().pokemon2()
        
        
    def Puissance(self): 
        '''Méthode qui augmente ou diminue la puissance d'attaque du pokemon1 : 
            pokemon1 -> pokemon du joueur
            pokemon2 -> adversaire
           
           Selon le type du pokemon1 et de l'adversaire l'attaque sera multiplié par 0.5, 1 ou 2 
        (voir tableau de l'énoncé).
        '''
              
        if self.type_pokemon2 == 'Normal' or \
           self.type_pokemon1 == self.type_pokemon2:
            
            self.attaque_pokemon2_= self.attaque_pokemon2
            return self.attaque_pokemon1
        
        elif self.type_pokemon1 == 'Eau' and self.type_pokemon2 == 'Feu' or \
             self.type_pokemon1 == 'Feu' and self.type_pokemon2 == 'Sol' or \
             self.type_pokemon1 == 'Sol' and self.type_pokemon2 == 'Eau':
            
            self.attaque_pokemon2_ = self.attaque_pokemon2 * 0.5
            return self.attaque_pokemon1 * 2

        elif self.type_pokemon1 == 'Eau' and self.type_pokemon2 == 'Sol' or \
             self.type_pokemon1 == 'Sol' and self.type_pokemon2 == 'Feu' or \
             self.type_pokemon1 == 'Feu' and self.type_pokemon2 == 'Eau':
            
            self.attaque_pokemon2_ = self.attaque_pokemon2 * 2
            return self.attaque_pokemon1 * 0.5
        
        elif self.type_pokemon1 == 'Normal':
            
            self.attaque_pokemon2_ = self.attaque_pokemon2 * 0.75
            return self.attaque_pokemon1 * 0.75
        
    def attaqueLouper(self):
        '''Méthode qui calcule 1 chance sur 20 soit 5% de chance de rater son attaque'''

        #5% de chance de louper son attaque
        self.coup_rater = random.randint(1,20)
        if self.coup_rater == 1:
            return True
    
    def attaque(self):
        
        
        #sinon le script prend l'attaque en fonction des deux type et le multiplier a la defense de l'ennemi (c'est un nombre inferieur a 1)
        
        #Arrondi l'attaque au nombre superieur
        attaque_pokemon1 = round(self.Puissance()) 
        attaque_pokemon2 = round(self.attaque_pokemon2_)

        self.pv_pokemon1_ = self.pv_pokemon1-(attaque_pokemon2/self.defence_pokemon1) 
        self.pv_pokemon2_ = self.pv_pokemon2-(attaque_pokemon1/self.defence_pokemon2) 
        
        print(f"{self.nom_pokemon1} a perdu {self.pv_pokemon1_} pv. ")
        print(f"{self.nom_pokemon2} a perdu {self.pv_pokemon2_} pv. ")
    
    
    def gagnant(self):
        #Methode qui regard a chaque fin de tour si l'un des pokemon n'a plus de pv pour annoncer le gagnant et le perdant
        if self.pv_pokemon1_ <= 0:
            print(f"{self.nom_pokemon2} a gagné.")
            print(f"vous avez perdu :( ")
        elif  self.pv_pokemon2_ <= 0:
            print(f"vous avez gagné ! :)")
            print(f"{self.nom_pokemon1} a perdu. ")
    
    
    def Fight(self) :
        
        while True:
            self.attaque()
            
            if self.attaqueLouper() == True :
                print('attaque louper')
            
            elif self.pv_pokemon2_ <= 0 :
                self.gagnant()
                break
            elif self.pv_pokemon1_ <= 0:
                self.gagnant()
                break   
        print(self.pv_pokemon1)

combat=Combat()

combat.Fight()
    