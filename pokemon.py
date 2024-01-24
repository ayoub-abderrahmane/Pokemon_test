import json
class Test:
    def __init__(self):
            self.data = []
            with open('pokedex.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        

    def affichage(self):
        print(self.data[1] ,{"name"})

test = Test()
test.affichage()