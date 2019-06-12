# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 09:50:04 2019

@author: nabha
"""

fruits = ["apple","pears","avacado","banana","strawberry","fig","cherry","date","prune","mango","orange","pineapple"]
numbers = ["1","54","536","2435","768","32323","09","98","65","34"]

numbers2 = [1,54,536,2435,768,32323,9,98,65,34]

deadstatus = [1,0,0,0,0,0,0,0,0,0,0,0,0,0]


#iteration 1 of list

#for fruit in fruits:
  #  print(fruit)
    
#for i in fruits:
#    i = fruits(1+i)
#    print(i)
 

step = 3
maxlen = len(fruits)
    
#for i in range(0,maxlen,step):
 #   print(fruits[i])
    
    
maxlen = len(numbers2)
total = 0


#for i in range(0,maxlen,1):
 #   print(numbers2[i])
  #  total += numbers2[i]
  
    
#print("total is: " + str(total))

#print ("Sum: " + str(sum(numbers2)))

#print ("All alive: " + str(all(deadstatus)))

j=0

for i in range(0,maxlen,1):
    if numbers2[i] > numbers2[j]:
        j = j+1
        print(numbers2[j])