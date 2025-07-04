from Deck import Deck
from Face import face
from Card import Card
def sum(list):
    counter = 0
    a = 0
    for i in range(len(list)):
        list[i]
        if list[i].number > 10:
            counter = counter +  10
        elif list[i].number < 11 and list[i].number > 1:
            counter = counter + list[i].number
        elif list[i].number == 1:
            counter = counter + 1
            a = a + 1
    for j in range(a):
        if 10 + counter <=  21:
            counter = counter + 10
    return counter
def printhand(list):
    for i in range(len(list)):
        print(list[i].__str__() + ",", end = "")
    print()

d = Deck()
d.shuffle()

while True:
    playerhand = [d.draw(),d.draw()]
    dealerhand = [d.draw(),d.draw()]
    while sum(playerhand) < 21:
        printhand(playerhand)
        print(sum(playerhand))
        h = input("Do you want to hit or stay?")
        if h == ("hit"):
            playerhand.append(d.draw())
        elif h == ("stay"):
            break
        else:
            print("invalid")
    while sum(dealerhand) < sum(playerhand) and sum(dealerhand) < 21:
        dealerhand.append(d.draw())
    print("The player's hand: ")
    printhand(playerhand)
    print("The dealer's hand: ")
    printhand(dealerhand)
    if sum(playerhand) == 21:
        print("You got BlackJack!!")
        face
    if sum(dealerhand) == 21:
        print("The Dealer got Black Jack!!")
    if sum(playerhand) > 21:
        print("You busted!")
    elif sum(dealerhand) > 21:
        print("The Dealer busted!")
    else:
        if sum(playerhand) > sum(dealerhand):
            print("You win!")
            face
        elif sum(dealerhand) > sum(playerhand):
            print("The dealer wins")
        else:
            print("Tie")
    s = input("Do you want to play another game?")

    if s == "no":
        break
    if s == "yes":
        d = Deck()
        d.shuffle()

