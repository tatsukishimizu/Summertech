def sort(list):
    smallest = 0
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[smallest] > list[j]:
                smallest = j
        x = list[i]
        list[i] = list[smallest]
        list[smallest] = x




        smallest = i + 1
list = [4,12,9,1,6,0,2]
sort(list)
print(list)

