#O(n)
def findcommon(lst1,lst2):
    nums = dict()
    commonval = []
    
    for x in lst1: 
        nums[x % 71] = [x]
    
    for y in lst2: 
        if y % 71 in nums:
            nums[y % 71].append(y)
        else:
            nums[y % 71] = [y]

        if len(nums [y % 71]) > 1:
            if nums [y % 71]:
                commonval.append(nums [y % 71][0])         
    return set(commonval)


print(findcommon([1,2,3,5,6,7,9],[3,4,2,5,3]))
    