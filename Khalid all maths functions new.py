#declaring global variables

#string lists
fruits = ["apple","pears","avacado","banana","strawberry","fig","cherry","date","prune","mango","orange","pineapple"]
numbers = ["1","54","536","2435","768","32323","09","98","65","34"]

#integer lists
deadstatus = [1,0,0,0,0,0,0,0,0,0,0,0,0,0]
numbers1 = [12, 45, 64, 98, 34,98,98,98,98,98,98]
numbers2 = [1,54,536,2435,76448,32323,9,98,65,1]
numbers3 = [14236,56,7,568,67,96,8,3,2,57,58,698,69,7807895678,567,57,2,6,45,47656]

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
    newsum = 0
    
    for i in range(0,len(x)):
        newsum =+ x[i]
    
    averagenumber = newsum/len(x)
    
    return averagenumber


#a function to find the most common number (mode)
def modearray(x):
    return modearray



#a function to find the median number in a list
def medianarray(x):
    
    halflength = len(x)/2
    
   # if  is 0 or 2 or 4 or 6 or 8:
        
    
    return halflength
    

#print(maxnumber2(x))
#print(minnumber(x))
#print(sumarray(x))
#print(averagearray(x))
print(medianarray(x))