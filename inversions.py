# Uses python3
import sys

def _mergeSort(arr, temp_arr, left, right): 
	print("_MERGESORT CALLS")
	print(" A variable inv_count is used to store inversion counts in each recursive call ")
	print("Array",arr,"Temp Arr",temp_arr)
	inv_count = 0
	print("INV_COUNT",inv_count)
	
	if left < right: 
		mid = (left + right)//2
		print("left,right,mid",left,right,mid)

		# It will calculate inversion counts in the left subarray 
		print("LEFT CALLED")
		print("INVERSIONS",inv_count)

		inv_count += _mergeSort(arr, temp_arr, left, mid) 

		print("RIGHT CALLED")
		# It will calculate inversion counts in right subarray 
		print("INVERSIONS",inv_count)
		inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 

		# It will merge two subarrays in a sorted subarray 
		print("MERGE CALLED")
		print("INVERSIONS",inv_count)
		
		inv_count += merge(arr, temp_arr, left, mid, right) 
		print("END OF _mergesort")
	return inv_count 

# This function will merge two subarrays in a single sorted subarray 
def merge(arr, temp_arr, left, mid, right): 
	print(left,mid,right)
	print("Merge Function Called")

	i = left	 # Starting index of left subarray 
	j = mid + 1 # Starting index of right subarray 
	k = left	 # Starting index of to be sorted subarray 
	inv_count = 0

	# Conditions are checked to make sure that i and j don't exceed their 
	# subarray limits. 

	while i <= mid and j <= right: 

		# There will be no inversion if arr[i] <= arr[j] 

		if arr[i] <= arr[j]: 
			temp_arr[k] = arr[i] 
			k += 1
			i += 1
		else: 
			# Inversion will occur. 
			temp_arr[k] = arr[j] 
			inv_count += (mid-i + 1) 
			k += 1
			j += 1

	# Copy the remaining elements of left subarray into temporary array 
	while i <= mid: 
		temp_arr[k] = arr[i] 
		k += 1
		i += 1

	# Copy the remaining elements of right subarray into temporary array 
	while j <= right: 
		temp_arr[k] = arr[j] 
		k += 1
		j += 1

	# Copy the sorted subarray into Original array 
	for loop_var in range(left, right + 1): 
		arr[loop_var] = temp_arr[loop_var] 
		
	return inv_count
	
if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	b = n * [0]
	print("MAIN FUNCTION")
	print(_mergeSort(a, b, 0, n-1))