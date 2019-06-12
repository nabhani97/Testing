#This program will greet and ask for your name.
#It'll then calculate the amount of characters in your name.
#Next it will ask for your age and then produce a personalised response.
#In that response it'll calculate in how many years you'll turn 100
#Lastly, it'll say goodbye


#Print texts that will pose as a question
print('Hi there!')
print('What is your name?')

#Prompt for an input from the user
myName=input()

#Create a space using the following print function
print()

#Using the inputted name as a variable, it'll create the response
print('It is great to meet you ' + myName + '!')
print('Wow, you have ' + str(int(len(myName))) + ' characters in your name!')

#Now asking for their age
print('Now, may I ask what is your age?')
myAge = int(input())

#Using an if statement, create a personalised response depending on input
print()
if myAge > 50:
    print(myName + ', you\'re pretty old! Did you know you will be 100 in ' + str(100-int(myAge)) + ' years time?')

elif myAge <= 50 and myAge > 25:
    print(myName + ', you\'re in your middle ages now! Did you know you will be 100 in'  + str(100-int(myAge)) + ' years time?')
    
elif myAge > -1:
    print(myName + ', you\'re still so young! Did you know you will be 100 in ' + str(100-int(myAge)) + ' years time?')

else:
    print('Sorry, you have inputted an invalid age!')
    
#Say goodbye
print()
print('Well, it was great meeting you ' + myName + ', I hope we can meet again sometime soon!')