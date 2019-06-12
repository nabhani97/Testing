# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:44:41 2018

@author: nabha
"""

# dictionaries

person = { 'age': 26, 'height':177, 'weight':77, 'name':'Jack', 'nickname':'J'}        # dictionary    data structure name/value pairs

# Output: Jack
print(person['name'])

# Output: 26
print(person.get('age'))


person['occupation'] = 'Plumber' 

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']

# add data to a dict
person['age'] = 40
print(person.get('age'))
