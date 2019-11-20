# Uses python3
import sys
def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
	a=0
	b=1
	if n<0:
		print("Invalid Input")
	elif n==0:
		return a
	elif n==1:
		return b
	else:
		for i in range(2,n+1):
			c=a+b
			a=b
			b=c
		return c

n = int(input())
print(calc_fib_fast(n))
