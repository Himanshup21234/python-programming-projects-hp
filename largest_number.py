#Uses python3

import sys
#from itertools import permutations 

def largest_Number(a): 
	tmp, ans = [], "" 
	#print(array)
	l = len(str(max(a))) + 1
	#print(l)
	for i in a:
		#print(i)
		temp = str(i) * l 
		#print(temp,temp[:l])
		tmp.append((temp[:l], i))
	tmp.sort(reverse = True)
	for i in tmp: 
		ans += str(i[1])		   
	return ans
		  
if __name__ == '__main__':
	input = sys.stdin.read()
	data = input.split()
	a = data[1:]
	print(largest_Number(a))
	#largestNumber(a)
