import sys
def mergesortList(numbers):
  if len(numbers)>1: 
    middle = len(numbers)//2
    leftList = numbers[:middle]
    rightList = numbers[middle:]
    mergesortList(leftList)
    mergesortList(rightList)
    i=j=k=0
    while i<len(leftList) and j<len(rightList):
      if leftList[i]<rightList[j]:
        numbers[k]=leftList[i]
        i+=1
      else:
        numbers[k]=rightList[j]
        j+=1
      k+=1
    while i<len(leftList):
      numbers[k]=leftList[i]
      i+=1
      k+=1
    while j<len(rightList):
      numbers[k]=rightList[j]
      j+=1
      k+=1
  return numbers
if __name__=="__main__":
	#numbers=input("Enter list of numbers separated by comma to sort:")
	numbers="0,5,2,12,45,4,10"
	try:
		listOfValues = [int(i) for i in numbers.split(",")]
		sortedList = mergesortList(listOfValues)
		print("Sorted numbers are: ", ",".join([str(i) for i in sortedList]))
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise
