#worst time is O(n)

def findPairs(arr1, arr2, x): 
    s1 = set(arr1)
    s2 = set(arr2)
    for y in s2:
        diff = x-y
        if (diff in s1):
            print("First number: ", y,"Second number: ", x-y, "sum",x)
  
arr1 = [1, 0, -4, 7, 6, 4] 
arr2 = [0, 2, 4, -3, 2, 1] 
x = 8

findPairs(arr1, arr2, x) 