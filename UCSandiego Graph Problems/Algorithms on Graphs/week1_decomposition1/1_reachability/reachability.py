#Uses python3

import sys
import time 

# Professor Approach 

#def reach(adj, x, y):
#    #write your code here
#    visited = [0] * len(adj)
#    return explore(adj, x, y, visited)
#	
#def explore(adj, x, y, visited):
#    if (x == y):
#        return 1
#    visited[x] = 1
#    for i in xrange(len(adj[x])):
#        if (not visited[adj[x][i]]):
#            if(explore(adj, adj[x][i], y, visited)):
#                return 1
#    return 0
   
def reach(adj, x, y):
    st=time.time()
    #print(st)
    #print(adj,x,y)
    visit = []
    explored = []
    visit.append(x)
    while visit:
        #print("Visit",visit)
        vertex = visit.pop()
        if vertex in explored: continue
        if vertex == y:
            return 1
        explored.append(vertex)
        #print("Explored",explored)
        for k in adj[vertex]:
            visit.append(k)
    if time.time()-st >= 5.0:
        print("Time Limit Exceeded",time.time()-st)
    else:
        print("Within time limits")
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    #print(n,m,data)
    #print(data[0:(2 * m):2])
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #print(edges)
    x, y = data[2 * m:]
    #print(x,y)
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    #print(adj)
    for (a, b) in edges:
        #print(a,b)
        #print(adj)
        adj[a - 1].append(b - 1)
        #print(adj)
        adj[b - 1].append(a - 1)
        #print(adj)
    print(reach(adj, x, y))
