# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    
    result = []
    for i in range(0, n+1):
        result.append(0)
    
    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 2 == 0:
            min2 = result[int(i/2)]
        if i % 3 == 0:
            min3 = result[int(i/3)]
        minOp = min(min1, min2, min3)

        result[i] = minOp + 1
        
    ops=result
    print(ops)
    sequence = []
    while n > 0:
        print("While n= ",n)
        sequence.append(n)
        print("sequence = ",sequence)
        if n % 2 != 0 and n % 3 != 0:
            print("While not 2 and 3 n= ",n)
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0: 
            print("While 2 and 3 n= ",n)
            n = n // 3
        elif n % 2 == 0:
            print("While 2 n= ",n)
            print(ops)
            if ops[n-1] < ops[n//2]: 
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0: 
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return reversed(sequence)
    
# input = sys.stdin.read()
# n = int(input)
# n=8
result = list(optimal_sequence(n))
print(len(result)-1)
for x in result:
    print(x, end=' ')