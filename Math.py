def add(x,y):
    if y == 0:
        return x
    return add(x,(y - 1)) + 1
print(add(5,3))