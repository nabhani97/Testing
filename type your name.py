#Program to keep asking for you to type 'your name'

print('Please type your name.')

name = input()

while name != 'your name':
    name = input()
    print('No, please type your name.')

print('Finally!')