import random
from pokemon import Pokemon

class Combat(Pokemon):

    def __init__(self):
        super().__init__()
        super().pokemon1()
        super().pokemon2()
        self.degat1 = []
        self.degat2 = []
    


        
    def Puissance(self,pokemon): 
        '''Méthode qui augmente ou diminue la puissance d'attaque du pokemon1 : 
            pokemon1 -> pokemon du joueur
            pokemon2 -> adversaire
           
           Selon le type du pokemon1 et de l'adversaire l'attaque sera multiplié par 0.5, 1 ou 2 
        (voir tableau de l'énoncé).
        '''
              
        if self.type_pokemon2 == 'Normal' or \
           self.type_pokemon1 == self.type_pokemon2:
            
            self.attaque_pokemon2_= self.attaque_pokemon2
            self.attaque_pokemon1
            match pokemon :
                case 1:
                    return self.attaque_pokemon1 
                case 2 :
                    return self.attaque_pokemon2_
        
        elif self.type_pokemon1 == 'Eau' and self.type_pokemon2 == 'Feu' or \
             self.type_pokemon1 == 'Feu' and self.type_pokemon2 == 'Sol' or \
             self.type_pokemon1 == 'Sol' and self.type_pokemon2 == 'Eau':
            
            self.attaque_pokemon2_ = self.attaque_pokemon2 * 0.5
            self.attaque_pokemon1_ = self.attaque_pokemon1 * 2
            match pokemon :
                case 1:
                    return self.attaque_pokemon1_ 
                case 2 :
                    return self.attaque_pokemon2_
        
        elif self.type_pokemon1 == 'Eau' and self.type_pokemon2 == 'Sol' or \
             self.type_pokemon1 == 'Sol' and self.type_pokemon2 == 'Feu' or \
             self.type_pokemon1 == 'Feu' and self.type_pokemon2 == 'Eau':
            
            self.attaque_pokemon2_ = self.attaque_pokemon2 * 2
            self.attaque_pokemon1_ = self.attaque_pokemon1 * 0.5
            match pokemon :
                case 1:
                    return self.attaque_pokemon1_ 
                case 2 :
                    return self.attaque_pokemon2_

        elif self.type_pokemon1 == 'Normal':
            
            self.attaque_pokemon2_ = self.attaque_pokemon2 * 0.75
            self.attaque_pokemon1_ = self.attaque_pokemon1 * 0.75
            match pokemon :
                case 1:
                    return self.attaque_pokemon1_
                case 2 :
                    return self.attaque_pokemon2_
    
    def attaqueLouper(self):
        '''Méthode qui calcule 1 chance sur 20 soit 5% de chance de rater son attaque'''

        #5% de chance de louper son attaque
        self.coup_rater = random.randint(1,20)
        if self.coup_rater == 1:
            return True
    
    
    def attaque(self,nb):
                
        #Arrondi l'attaque au nombre superieur
        attaque_pokemon1 = round(self.Puissance(1))      
       
        if nb == 0:    
            self.pv_pokemon2_ = self.pv_pokemon2 - round(attaque_pokemon1/self.defence_pokemon2) 
            
            self.pv_restant2 =  self.pv_pokemon2 - self.pv_pokemon2_
            
            self.degat2.append(self.pv_restant2)
        
            print(self.degat2)
            print(f"{self.nom_pokemon2} a perdu {self.pv_pokemon2_} pv.{self.pv_restant2} ")
        
        else:
            self.pv_pokemon2_= self.degat2[nb-1] - round(attaque_pokemon1/self.defence_pokemon2) 
            
            self.pv_restant2 =  self.pv_pokemon2 - self.pv_pokemon2_
            
            self.degat2.append(self.pv_restant2)
            print(self.degat2)
            print(f"{self.nom_pokemon2} a perdu {self.pv_pokemon2_} pv.{self.pv_restant2} ")
   
    
    def contre_attaque(self,nb):
        #sinon le script prend l'attaque en fonction des deux type et le multiplier a la defense de l'ennemi (c'est un nombre inferieur a 1)
        
        #Arrondi l'attaque au nombre superieur
        attaque_pokemon2 = round(self.Puissance(2))       
        if nb == 0:    
            self.pv_pokemon1_ = self.pv_pokemon1 - round(attaque_pokemon2/self.defence_pokemon1) 
            
            self.pv_restant1 =  self.pv_pokemon1 - self.pv_pokemon1_
            
            self.degat1.append(self.pv_restant1)
        
            print(self.degat1)
            print(f"{self.nom_pokemon1} a perdu {self.pv_pokemon1_} pv.{self.pv_restant1} ")
        else:
            print(nb)
            self.pv_pokemon1_ = self.degat1[nb-1] - round(attaque_pokemon2/self.defence_pokemon1) 
            
            self.pv_restant1 =  self.pv_pokemon1 - self.pv_pokemon1_
            
            self.degat1.append(self.pv_restant1)
            print(self.degat1)
            print(f"{self.nom_pokemon1} a perdu {self.pv_pokemon1_} pv.{self.pv_restant1} ")
   
    def gagnant(self,i):
        #Methode qui regard a chaque fin de tour si l'un des pokemon n'a plus de pv pour annoncer le gagnant et le perdant
        if self.degat1[i] <= 0:
            print(f"{self.nom_pokemon2} a gagné.")
            print(f"vous avez perdu :( ")
            return True
        elif self.degat2[i] <= 0:
            print(f"vous avez gagné ! :)")
            print(f"{self.nom_pokemon1} a perdu. ")
            return True
        return False
    
    
    def Fight(self) :
        i=0
        while True:
            print (i) 
            if i % 2 == 0:
                print (i)  
                if self.attaqueLouper() == True :
                    print('attaque louper')
                    self.contre_attaque(i)
                self.attaque(i)
            else:
                if self.attaqueLouper() == True :
                    print('attaque louper')
                    self.attaque(i)
                self.contre_attaque(i)
                break
            # self.gagnant(i)    
            i = i+1
            print(i)
               
            
        
        

combat=Combat()

combat.Fight()
    