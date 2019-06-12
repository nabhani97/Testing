#while version of type your name python code

name = ''
attemptno = 2

print('Please type your name.')
name = input()
if name != 'your name':
    while name != 'your name':
        print('\nPlease try again.\n\nThis is attempt number: ' + str(int(attemptno)))
        name = input()
        attemptno = attemptno + 1
        
    print('Finally!')


else:
    print('You got it on your first try! Nice one!')