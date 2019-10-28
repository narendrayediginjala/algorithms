import sys
def sortList(numbers):
	try:
		for i in range(len(numbers)-1,0,-1):
			for j in range(i):
				if numbers[j]>numbers[j+1]:
					temp = numbers[j+1]
					numbers[j+1]=numbers[j]
					numbers[j]=temp
			print("Current Iteration list:",numbers)
		return numbers
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

if __name__=="__main__":
	#numbers=input("Enter list of numbers separated by comma to sort:")
	numbers="0,5,2,12,45,4,10"
	try:
		listOfValues = [int(i) for i in numbers.split(",")]
		sortedList = sortList(listOfValues)
		print("Sorted numbers are: ", ",".join([str(i) for i in sortedList]))
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise
