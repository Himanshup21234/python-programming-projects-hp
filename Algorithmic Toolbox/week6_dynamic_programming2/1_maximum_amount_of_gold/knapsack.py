# Uses python3
import sys

def optimal_weight(W, wt,val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[n][W] 
    
def optimal_weight_val(capacity, bars):
    amount = len(bars)
    value=[[0 for row in range(0, amount+1)] for col in range(0, capacity+1)]
    for i in range(1, amount+1):
        wi = bars[i-1]
        vi = bars[i-1]
        for w in range(1, capacity+1):
            value[w][i] = value[w][i-1]
            if wi <= w:
                val = value[w-wi][i-1] + vi
                if value[w][i] < val:
                    value[w][i] = val
    return value[capacity][amount]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    val= [1]*  n
    #print(optimal_weight(W, w,val,n))
    print(optimal_weight_val(W,w))