# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_pisano_period(m):
	a,b=0,1
	for i in range(m*m):
		a,b=b,(a+b)%m
		if a==0 and b==1:
			return i+1
	return m
		
def get_fibonacci_huge(n, m):
    m= get_pisano_period(m)
    n=n%m
    previous = 0
    current = 1
    if n <= 1:
        return n
    for i in range(2,n + 1):
        previous, current = current, previous + current
    return current

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(int(get_fibonacci_huge(n, m)%m))
