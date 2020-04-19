numbers1 = [1,6,3,5,7,3,2,7]
numbers2 = [1,3,7,5,5,2,2,7]
#supposed to get [1,5,2,7]
#time complexity is O(n)... very bad!
def findSameVals (list1,list2):
    sameVals=[]
    i = 0
    while i < len(numbers1):
        if numbers1[i]==numbers2[i]:
            sameVals.append(numbers2[i])
        i+=1
    sameVals2 = set(sameVals)
    return sameVals

print(findSameVals(numbers1,numbers2))