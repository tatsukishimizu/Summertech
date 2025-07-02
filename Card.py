class Card:
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
    def __str__(self):
        if self.number == 1:
            return "Ace of " + self.suit + "s"
        if self.number == 11:
            return "Jack of " + self.suit + "s"
        if self.number == 12:
            return "Queen of " + self.suit + "s"
        if self.number == 13:
            return "King of " + self.suit + "s"
        return str(self.number) + " of " + self.suit + "s"
    
        



x = Card(7,"Club")
print(x)
    
