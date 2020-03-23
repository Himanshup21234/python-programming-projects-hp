# Uses python3
import sys

def binary_search(a, x):
	#a.sort()
	#print(a)
	left, right = 0, len(a)-1
	# write your code here
	while left <=right:
		#print(left,right)
		mid= left+ (right-left)//2
		#print(mid)
		if a[mid]==x:
			return mid
		elif a[mid]<x:
			left = mid+1
		else:
			right=mid-1
	return -1

def linear_search(a, x):
	for i in range(len(a)):
		if a[i] == x:
			return i
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	#print(data)
	n = data[0]
	m = data[n + 1]
	a = data[1 : n + 1]
	#print(n,m,a)
	for x in data[n + 2:]:
		# replace with the call to binary_search when implemented
		print(binary_search(a, x), end = ' ')