def isMonotonic(array):
	if len(array)>2:
		result=True
		for i in range(2,len(array)):
			if array[i]>array[i-1] and array[i-1]<array[i-2]:
				result=False
			elif array[i]<array[i-1] and array[i-1]>array[i-2]:
				result=False
		return result
	else:
		return True
if __name__=="__main__":
  assert isMonotonic([-1,-2,-3,-4,-5])==True