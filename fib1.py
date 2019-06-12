#from typing import Dict
#memo: Dict[int,int] = {0:0, 1:1}
memo = {0:0, 1:1}
# recursion or a recursive function
def fib3(n:int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]



def fib1(n:int) -> int:
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)

#print (memo)
x = fib3(50)
#print (memo)


print ("Result: " + str(x))