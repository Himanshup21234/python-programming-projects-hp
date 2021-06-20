#Uses python3
import sys
import time
def number_of_components(adj):
    st=time.time()
    result=0
    print(adj)
    if time.time()-st >= 5.0:
        print("Time Limit Exceeded",time.time()-st)
    else:
        print("Within time limits")
        
    #write your code here
    visit=[]
    explored=[]
    visit.append(adj[0])
    while visit:
        print(visit)
        vertex=visit.pop()
        if vertex in explored: continue
        if vertex ==y :
            return 1
        for k in adj[ver]:
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
