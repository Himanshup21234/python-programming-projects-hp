# Uses python3
import sys

denom=[1, 5, 10]

def get_change(m):
	cnt=0
	i=len(denom)-1
	preval=m
	while i >= 0:
		#print(i,m,denom[i])
		while m >=denom[i]:
			#print(m)
			m=m-denom[i]
			cnt+=1
		i-=1
	return cnt

if __name__ == '__main__':
	m = int(sys.stdin.read())
	print(get_change(m))
