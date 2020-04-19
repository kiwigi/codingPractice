numbers1 = [1,6,3,5,7,3,2,7]
numbers2 = [1,3,7,5,5,2,2,7]
#supposed to get [1,3,5,2,7]
#time complexity is n^2... very bad!
def findSameVals (list1,list2):
    sameVals=[]
    for x in list1:
        print("x:",x)
        for y in list2:
            print("y:",y)
            if x==y:
                sameVals=sameVals+[x]
                print(sameVals)
    sameVals2 = set(sameVals)
    return sameVals2

print(findSameVals(numbers1,numbers2))