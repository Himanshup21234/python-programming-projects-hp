# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:23:32 2020

@author: AW639XJ
"""
import time

def memoize_factorial(f): 
    memory = {} 
    print("Memoize Started")
    def inner(num): 
        print("Inner of Inner",memory)
        print("Num = ",num)
        if num not in memory:
            print("Calling Function fib")
            memory[num] = f(num) 
            print("Memory",memory)
        return memory[num] 
    print("Outside of Inner",inner)
    print("Memoize End")
    return inner 

@memoize_factorial
def fib(n):
    print("n= ",n)
    print("Fibonaci Started")
    if n<=1:
        print("Return n=",n)
        return n
    print("End Fibonaci")
    return fib(n-1) + fib(n-2)

start=time.time()
# print(time.time())
for i in range(2,10):
    print("Loop = ",i)
    print(fib(i))
print((time.time()-start))

