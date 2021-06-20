# Uses python3
import sys

def get_change(coins,l,m):
    table=[0 for i in range(m+1)]
    table[0]=0
    # write your code here
    for i in range(1,m+1):
        table[i]=sys.maxsize
    # print(table)
    for i in range(1,m+1):
        for j in range(l):
            if coins[j]<=i:
                sub_res=table[i-coins[j]]
                # print("sub_res= ",sub_res)
                # print("table[{}]= {}".format(str(i),str(table[i])))
                if sub_res!=sys.maxsize and sub_res+1<table[i]:
                    table[i]=sub_res+1
                # if table[i]==coins[j]:
                    # break
        # print("Inner Loop End with table= ",table)
    return table[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m=11
    coins=[1,3,4]
    print(get_change(coins,len(coins),m))