from Card import Card
from random import randint
class Deck:
    def __init__(self):
        self.deck = []
        for i in range (1,14):
            self.deck.append(Card(i,"Heart"))
            self.deck.append(Card(i,"Club"))
            self.deck.append(Card(i,"Spade"))
            self.deck.append(Card(i,"Diamond"))
    def shuffle(self):
        for i in range(len(self.deck)):
            x =randint(0,len(self.deck) - 1)
            y = self.deck[x]
            self.deck[x] = self.deck[i]
            self.deck[i] = y
    def draw(self):
        return self.deck.pop()
    def getlength(self):
        return len(self.deck)
        



            

    
    
            
                
            
            

