def exponents(x,y):
    if y == 0:
        return 1
    return exponents(x,(y - 1)) * x
print(exponents(2,3))