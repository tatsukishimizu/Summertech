def multiplication(x,y):
    if y == 0:
        return 0
    return multiplication(x,(y - 1)) + x
print(multiplication(2,7))


