#This will be a program that will convert integer numbers into a string of words

#Declaring Global Variables
num0to19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight',"Nine", 'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
num20to99 = ['', '','Twenty','Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']



print('Hello')
print('')
print('Please enter a number to be converted into words:')

def num2words0to99(num):
    #print('num is equal to: ' + int(str(num)[1]))
    if 0 <= num <= 19:
        return num0to19[int(str(num)[-2:])]
    if 20 <= num <= 99:
        return num20to99[int(str(num)[-2])] + ' ' + num0to19[int(str(num)[-1])]

def num2words100to119(num):
    return num0to19[int(str(num)[-3])] + ' Hundred and ' + num2words20to99(num)



def num2words(num):
    
    if 0 <= num <= 99:
        return num2words0to99(num)
 
    if 100 <= num <= 119:
        return num2words100to119(num)


num1 = int(input())
numfin=num2words(num1)
print(numfin)



