#time complexity = O(n)

arr=['Ale.xandratenney@hotmail.ca', 'alexandratenney@hotmail.ca', 'alexandratenney+renee@hotmail.ca', 'mar@gmai.l.com','m+ar@gmai.l.com']

def findUnique(a1):
    newarr=[]
    for x in a1:
        print(x)
        newstr=x
        if (x.count('.')!=0):
            newstr = x.replace('.','')
            print(x)
        if (x.count('+')!=0):
            plus = newstr.index('+')
            at = (newstr.index('@'))
            sub = x[plus:at]
            newstr= newstr.replace(sub,'')
        newstr=newstr.lower()
        newarr.append(newstr)
    numOfUn=0
    arrs= set(newarr)
    numOfUn=len(arrs)
    return numOfUn

    
print(findUnique(arr))