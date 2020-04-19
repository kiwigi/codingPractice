#O(n^2)
def findSum(lst1,lst2, sum):
    for x in lst1:
        for y in lst2:
            if x+y== sum:
                return x,y

print(findSum([1,2,3],[5,6,7],10))
    