names = ["shana a","mr jingles", "please a no omg", "help 911"]

#fort by last name, alaphabetical
#O(nlogn)
def sortbylast(lst):
    i = 0
    #while(i < len(lst)):
    lst.sort(key = lambda name: name.split(" ")[-1])
        #i= i+1 
    return lst

print(sortbylast(names))