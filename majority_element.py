# Uses python3
import sys

def get_majority_element(a, left, right):
	temp={}
	c=0
	#if left == right:
	#	return -1
	#if left + 1 == right:
	#	return a[left]
	#write your code here
	for i in range(len(a)):
		if a[i] in temp:
			temp[a[i]]+=1
		else:
			temp[a[i]]=1
	for k in temp:
		if temp[k]>int(len(a)//2):
			c+=1
	if c >0:
		return c
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	#print(n,a)
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)
