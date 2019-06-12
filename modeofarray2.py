def modeofarray2(x):
    #x = [1,1,4,4,4,2,2]
    x = [43,25,345,345,43,56,56,356,34,3,3,3,33,4,3,3,4,235,5,3,3]
    
    listsort = sorted(x)
    
    currentindex = -1
    numtype = []
    numtally = []
    
    runnum = 1
    
    prevnum = -1
    
    print("-----------------------------Start-----------")
    print("the numbers: " + str(numtype))
    print("the tally: " + str(numtally))
    print("----------Loop is starting here-----------")
    
    for i in listsort:
        print("the number of runs is currently: " + str(runnum))
        if i == prevnum:
            numtally[currentindex] = numtally[currentindex] + 1
            
        else:
            numtype.append(i)
            numtally.append(1)
            currentindex += 1
            
        prevnum = i
        
        print("the number: " + str(numtype))
        print("the tally: " + str(numtally))
        
        runnum += 1
    
    print("FINISHED")
    print("the numbers final: " + str(numtype))
    print("the tally final: " + str(numtally))
    
    #here i am introducing the code to retrieve the actual mode
    
    highesttally = max(numtally)
    print("the max number in the tally is: " + str(highesttally))
    highesttallyindex = numtally.index(highesttally)
    print("the index of the max number in the tally is: " + str(highesttallyindex))
    actualmode = numtype[highesttallyindex]
    print("The actual mode is: " + str(actualmode))
    
    

print(modeofarray2(2))