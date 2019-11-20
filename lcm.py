# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_fast(a, b, gcd):
    return (a*b/gcd)

def gcd_fast(a, b):
	if b==0:
		return a
	else:
		return gcd_fast(b,a%b)

if __name__ == '__main__':
	input = sys.stdin.read()
	a, b = map(int, input.split())
	if a<b:
		c=a
		a=b
		b=c
	gcd=gcd_fast(a, b)
	print(int(lcm_fast(a, b,gcd)))