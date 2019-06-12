# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:56:32 2019

@author: nabha
"""

#list = [2,5,7,3,4,12,9]
list = [2,5,7,3,4,12,9,4,35,54,45,6,5,2,878,9,0]

x = 9999
found = 0


for i in range(0,len(list)):
    #print(i)
    print(list[i])
    if x == list[i]:
        found = 1

print('Found = ' + str(found))
print("Start")