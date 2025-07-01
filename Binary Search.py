def binarysearch(start,end,list,target):
        if start > end:
            return -1
        midpoint = (start + end)//2
        if list[midpoint] == target:
            return midpoint
        if target > list[midpoint]:
            return binarysearch(midpoint + 1, end, list, target)
        if target < list[midpoint]:
            return binarysearch(start, midpoint -  1, list, target)
sample = [2,5,7,9,17]
print(binarysearch(0,len(sample), sample, 17))    s