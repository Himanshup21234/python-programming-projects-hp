# python3
import random

def max_pairwise_product_fast(n, a):
      fast = 0
      min_index1 = -1
      for i in range(n):
          if min_index1 == -1 or a[i] < a[min_index1]:
              min_index1 = i

      min_index2 = -1
      for i in range(n):
          if i != min_index1 and (min_index2 == -1 or a[i] < a[min_index2]):
              min_index2 = i
      fast = a[max_index1] * a[max_index2]
      return fast

def max_pairwise_product(n, a):
            result = 0
            for i in range(0, n):
                for j in range(i + 1, n):
                    if a[i] * a[j] > result:
                        result = a[i] * a[j]
            return result


if __name__ == '__main__':
	#while True:
		n = int(input())
		a= [int(x) for x in input().split()]
		#print(max_pairwise_product_fast(n,a))
		#n = (random.randint(2, 11))
		#a = [random.randint(0, 99999) for r in range(n)]
		assert (len(a) == n)
		#result = max_pairwise_product(n, a)
		#fast=max_pairwise_product_fast(n, a)
		print(max_pairwise_product_fast(n,a))
		#print(fast, result, "OK")
		#if fast != result :
		#	break




