# Uses python3
import sys
import random
	
#def partition3(a, l, r):
#	#print("Partition2")
#	x = a[l]
#	#print("x=",x)
#	j = l
#	gt=r
#	#print("j=",j)
#	for i in range(l + 1, gt + 1):
#		#print("i",i)
#		#print("a[i] <= x",a[i],x,a[i] <= x)
#		if a[i] <x:
#			a[i], a[j] = a[j], a[i]
#			j += 1
#			#print("j",j)
#			#print("Array",a)
#		elif a[i] >x:
#			a[l], a[gt] = a[gt], a[l]
#			gt=gt-1
#			i=i-1
#		#	a[i], a[j] = a[j], a[i]
#	return j,gt

def partition3(A, l, r):
	print("Begin Partition3")
	lt = l
	i = l 
	gt = r
	pivot = A[l]
	print("Initialize Parameters",lt,i,gt)
	print("Begin Loop")
	while i <= gt:
		print("i= ",i)
		print("Before Check Array",A)
		if A[i] < pivot:
			print("a[i] < x",A[i],pivot,A[i] < pivot)
			A[lt], A[i] = A[i], A[lt]
			lt += 1
			i += 1
			print("After lt Check Array",A)
		elif A[i] > pivot:
			print("a[i] > x",A[i],pivot,A[i] > pivot)
			A[i], A[gt] = A[gt], A[i]
			gt -= 1
			print("Array gt check",A)
		else:
			i += 1
	return lt, gt
   

def partition2(a, l, r):
	#print("Partition2")
	x = a[l]
	#print("x=",x)
	j = l
	#print("j=",j)
	for i in range(l + 1, r + 1):
		#print("i",i)
		#print("a[i] <= x",a[i],x,a[i] <= x)
		if a[i] <=x:
			j += 1
			#print("j",j)
			a[i], a[j] = a[j], a[i]
			#print("Array",a)
		#elif a[i] ==x:
		#	r=r-1
		#	a[i], a[j] = a[j], a[i]
	a[l], a[j] = a[j], a[l]
	
	return j


def randomized_quick_sort(a, l, r):
	print("randomized_quick_sort called Array",a,l,r)
	if l >= r:
		return
	k = random.randint(l, r)
	print("Values",k,a[l], a[k])
	a[l], a[k] = a[k], a[l]
	print("Values",k,a[l], a[k])
	#use partition3
	m1,m2 = partition3(a, l, r)
	#m1 = partition2(a, l, r)
	randomized_quick_sort(a, l, m1 - 1);
	print("Call Rand 1")
	#randomized_quick_sort(a, m1, m2);
	##print("Call 1 End")
	randomized_quick_sort(a, m2 + 1, r);
	print("Call Rand 2")


if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	randomized_quick_sort(a, 0, n - 1)
	for x in a:
		print(x, end=' ')
