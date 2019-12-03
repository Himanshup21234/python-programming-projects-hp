# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	points = []
	sort_seg=sorted(segments,key=lambda x:x.end)
	while sort_seg:
		seg=sort_seg.pop(0)
		pt=seg.end
		points.append(pt)
		for s in sort_seg[:]:
			if s.start <= pt <=s.end:
				sort_seg.remove(s)
	print(len(points))		
	return points

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *data = map(int, input.split())
	#print(data)
	segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
	points = optimal_points(segments)
	for i in points:
		print(i,end=' ')
	#print("End",points)
	#print(len(points))
	#print(*points)
