# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	weight=0
	sort_val=[]
	for i in range(len(weights)):
		sort_val.append((values[i]/weights[i],weights[i],values[i]))
	sort_val=sorted(sort_val,reverse=True)
	#while capacity>0:
	for i in sort_val:
		if capacity==0:
			break
		elif capacity>=i[1] and capacity>0:
			value+=i[2]
			weight+=i[1]
			capacity-=i[1]
		elif capacity<=i[1] and capacity>0:
			value+=capacity*i[0]
			weight+=capacity
			capacity=0
	#print(value,weight,capacity)
	return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	#print(data)
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	#print(values)
	weights = data[3:(2 * n + 2):2]
	#print(weights)
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.4f}".format(opt_value))
