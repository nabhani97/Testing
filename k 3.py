
fruits = ["apple","pears","avacado","banana","strawberry","fig","cherry","date","prune","mango","orange","pineapple"]
numbers = ["1","54","536","2435","768","32323","09","98","65","34"]

numbers2 = [5,54,536,2435,768,32323,9,98,65,34]
deadstatus = [1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
maxlen = len(numbers2) - 1

j=0

for i in range(0,maxlen,1):
    if numbers2[i] >= numbers2[j]:
        j = j + 1

#print(j)

for i in range(0,maxlen,1):
    newnumbers2 = numbers2[i]
    print(numbers2[i])
print(i)
