# python3
import sys


def compute_min_refills(distance, tank, stops):
	# write your code here
	currRefills=0
	lastRefills=0
	numRefills=0
	stops.append(0)
	stops.append(distance)
	stops=sorted(stops)
	#print(stops)
	n=len(stops)-1
	#print(n)
	if distance <= tank:
		return 0
	else:
		while currRefills <n:
			#print("#",currRefills)
			lastRefills=currRefills
			while(currRefills<n and stops[currRefills+1]-stops[lastRefills] <=tank):
				#print("#",currRefills)	#print(currRefills,lastRefills,stops[currRefills+1],stops[lastRefills],stops[currRefills+1]-stops[lastRefills])
				currRefills+=1
			
			if currRefills==lastRefills:
				return -1
			elif currRefills<n and lastRefills<=n:
				numRefills+=1
			#print(numRefills)
	return numRefills

if __name__ == '__main__':
	d, m, _, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops))
