def countdown(hi):
    print(hi)
    if hi > 0:
        countdown(hi - 1)
countdown(998)        





def countup(x,y):
    print(x)
    if x < y:
        countup(x + 1,y)
countup(0,998)
