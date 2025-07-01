def sort(list):
    for i in range(len(list)):
        number = i
        while number > 0 and list[number] < list[number - 1]:
            x = list[number]
            list[number] = list[number - 1]
            list[number - 1] =  x
            number = number - 1
list = [8,7,4,8,3,1]
sort(list)
print(list)