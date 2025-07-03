from Deck import Deck
x = Deck()
x.shuffle()
score1 = 0
score2 = 0
while x.getlength() > 0:
    one = x.draw()
    print(one)
    two = x.draw()
    print(two)

    if one.number > two.number:
        score1 = score1 + 2
    if one.number < two.number:
        score2 = score2 + 2
    
    if one.number == two.number and x.getlength() > 0:
        draws = 0
        print("WAAAAARRR")
        while one.number == two.number:
            for i in range(4):
                one = x.draw()
                two = x.draw()
                draws = draws + 2
                if x.getlength == 0:
                    break
            print(one)
            print(two)
            if one.number > two.number:
                score1 = score1 + draws
            if one.number < two.number:
                score2 = score2 + draws
    input("Next Turn: Return") 
                
    
if score1 > score2:
    print("Player #1 wins!              OOOOOO           000000")
    print("                             OOOOOO           000000")
    print("                             OOOOOO           000000")
    print("                                                             ")
    print("                                                             ")
    print("                              ii                  ii")
    print("                               ii                ii")
    print("                                 iiiiiiiiiiiiiiii")
elif score2 > score1:
    print("PLayer#2 wins!")
else:
    print("Tie!")

                                        
                                    

            
        

    
    



















































