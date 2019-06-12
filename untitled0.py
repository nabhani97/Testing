#declaring global variables

#string lists
fruits = ["apple","pears","avacado","banana","strawberry","fig","cherry","date","prune","mango","orange","pineapple"]
numbers = ["1","54","536","2435","768","32323","09","98","65","34"]

#integer lists
deadstatus = [1,0,0,0,0,0,0,0,0,0,0,0,0,0]
numbers1 = [12, 45, 64, 98, 34, 56]
numbers2 = [1,54,536,2435,76448,32323,9,98,65,1]
numbers3 = [14236,56,7,568,67,96,8,3,2,57,58,698,69,7807895678,567,57,2,6,45,47656]
smallarray = [1,6,7,4,3]

#testing the specific list:
x = numbers1

arraylen = len(x)
#print (arraylen)      #length of list in Python terms



#a function to return maximum number in list
def maxnumber(x):
    maxnum = 0
    print('maxnum before loop is: ' + str(maxnum))
    
    for i in range(0, len(x)):
        print('i  is: ' + str(i) + ', maxnum is: '+ str(maxnum))
        
        if x[i] >  maxnum:
            print("---> changing maxnum to: " + str(x[i]))
            maxnum = x[i]
            
    return maxnum


#more efficient version of maxnumber
def maxnumber2(x):
    maxnum = 0
    
    for i in range(0, len(x)):        
        if x[i] > maxnum:
            maxnum = x[i]            
    return maxnum


#a function to return minimum number in list
def minnumber(x):
    counter = 0
        
    for i in range(0,maxlen,1):
        if x[i] <= x[counter]:
            counter = counter + 1

    return x[counter]
    


#a function to return sum of all numbers in list
def sumarray(x):
    newsum = 0
    
    print ("before loop: newsum = " + str(newsum))
    
    for i in range(0,len(x)):        
        print("i is: " + str(i) + ", number is: " + str(x[i]) + ", newsum is: " + str(newsum))
        newsum += x[i]

    print ("after loop: newsum = " + str(newsum))

    return newsum


#a function to return the average of of a list
def averagearray(x):
   # newsum = 0
    
#    for i in range(0,len(x)):
 #       newsum =+ x[i]
    
    averagenumber = sumarray(x)/len(x)
    return averagenumber


#a function to find the most common number (mode)
def modearray(x):
    return modearray



#a function to find the median number in a list
def medianarrayOLD(x):
    median = 0
    
    if (len(x) % 2 == 0):  # even
        half = len(x)/2
        half = int(half - 1)    # short form: half += 0.5
        first = x[half]
        second = x[half + 1]
        total = first + second
        median = total / 2
    else:                    # odd
        half = len(x)/2
        half = int(half - 0.5)    # short form: half += 0.5
        print ("Half: " + str(half))
        median = x[half]
    
   # if  is 0 or 2 or 4 or 6 or 8:
    return median
    
# new and improved version
def medianarray(x):
    median = 0

    half = len(x)/2
    
    if (len(x) % 2 == 0):  # even
        median =  (x[int(half - 1)] + x[int(half)]) / 2
    else:                    # odd
        median = x[int(half - 0.5)]    # short form: half += 0.5

    return median


def modeofarray(x):
    x = [2,1,4,1,4,2,2]
    typesofnum = [1,2,4]
    tallyofnums = [0,0,0]
    
    ones = 0
    twos = 0
    fours = 0
    themax = 0
    numtype = 0
    
    for i in range(0,len(x)):
        if (x[i] == 1):
            ones = ones + 1
        elif (x[i] == 2):
            twos = twos + 1
        elif (x[i] == 4):
            fours = fours + 1
    
    print ("Ones: " + str(ones))
    print ("Twos: " + str(twos))
    print ("Fours: " + str(fours))
    
    if (ones > themax):
        themax = ones
        numtype = 1
    if (twos > themax):
        themax = twos 
        numtype = 2
    if (fours > themax):
        themax = fours
        numtype = 4
        
    print ("Max: " + str(themax) + ", type: " + str(numtype))
    
    
    return numtype
    
def modeofarray2(x):
    x = [2,1,4,4,2,2]
    #x = [12,3,12,56,3,12,66,88,44,88,100,1000,100,88,88,88,88,88,88,12,3,12]
    numsorted = sorted(x)
    
    theindex = -1
    thenumbers = []
    thetallies = []

    therun = 1
    
    prevNumber = -1 
    print(" --- Start --------------------")            

    print("The numbers:" + str(thenumbers))
    print("The tallies:" + str(thetallies))

    # assertions 
    assert(len(thenumbers) == 0)
    assert(len(thetallies) == 0)

    print(" --- Just before loop --------------------")            
    for i in numsorted:
        print(">>>> The Run: " + str(therun))
        if i == prevNumber:
            # number is same - increment tally= 
            thetallies[theindex] = thetallies[theindex] + 1 
        else:
            # add new number to array
            thenumbers.append(i)
            thetallies.append(1)
            theindex += 1
        
        prevNumber = i
            
        print("The numbers:" + str(thenumbers))
        print("The tallies:" + str(thetallies))
        therun += 1

    print(" --- Finished --------------------")            
    print("The numbers:" + str(thenumbers))
    print("The tallies:" + str(thetallies))




#print(maxnumber2(x))
#print(minnumber(x))
#print(sumarray(x))
#print(averagearray(x))
#print(medianarray(smallarray))
print (modeofarray2(x))

