def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    temp: int = 0
    
    for i in range(1,n):
        print("Loop:" + str(i))
        #temp = last
        #last = next
        #next = temp + next
        #print("temp: " + str(temp))
        #print("last: " + str(last))
        #print("next: " + str(next))
        last, next = next, last + next
    return next


x = fib5(6)
#print (memo)

print ("Result: " + str(x))


