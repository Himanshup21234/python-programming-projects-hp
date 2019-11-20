# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    #print(n)
    for _ in range(2,n+1):
        previous, current = current, previous + current
        #print(current%10,end=" ")
    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n%60))
