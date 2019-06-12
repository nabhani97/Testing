def modeofarray2():
    #x = [2,2,2,3,4,5,5]
    x = [32423,435,345,35,6546,4566,54654654654,6,5,5,5,5,5645]
    
    listsort = sorted(x)
    numtype = []
    numcount = []
    prevnum = -1
    currentindex = -1
    
    for i in listsort:
        
        if i == prevnum:
            numcount[currentindex] = numcount[currentindex] + 1
        
        else:
            numtype.append(i)
            numcount.append(1)
            currentindex += 1
    
        prevnum = i
        
    print("final number types: " + str(numtype))
    print("final number counts: " + str(numcount))
    
    maxcount = max(numcount)
    print("the highest amount of times a number has repeated: " + str(maxcount))
    maxcountindex = numcount.index(maxcount)
    print("the index of the highest freq number is: " + str(maxcountindex))
    actualmode = numtype[maxcountindex]
    print("Finaly, the mode of our list is: " + str(actualmode))
    
    return actualmode

print(modeofarray2())