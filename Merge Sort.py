def recursion(list,l,r):
    midpoint = (l + r)//2
    if l == r:
         return
    else:
        recursion(list,l,midpoint )
        recursion(list,midpoint + 1,r)
        merge(list,l,r)


def merge(list,l,r):
    array = []
    midpoint = (l + r)//2
    targetl = l
    targetr = midpoint + 1
    while targetl < midpoint + 1 and targetr < r + 1:
        if list[targetl] < list[targetr]:
            array.append(list[targetl])
            targetl = targetl + 1
        else:
            array.append(list[targetr])
            targetr =  targetr + 1
    while targetl < midpoint + 1:
            array.append(list[targetl])
            targetl = targetl + 1
    while targetr < + 1:
         array.append(list[targetr])
         targetl = targetl + 1
    for i in range(len(array)):
         list[i + l] = array[i]

list = [6,3,68,3,6,8,4,]
recursion(list,0,len(list) - 1)
print(list)
                     
