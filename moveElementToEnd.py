def moveElementToEnd(array, toMove):
    # Write your code here.
  front=0
  end=len(array)-1
  while end>front:
    if array[front]==toMove and array[end]!=toMove:
      array[front],array[end]=array[end],array[front]
    else:
	    if array[front]!=toMove:
		    front+=1
	    if array[end]==toMove:
		    end-=1
  return array
if __name__=="__main__":
  assert moveElementToEnd([1,3,5,6,7,9],5)==[1,3,9,6,7,5]
  assert moveElementToEnd([1,3,5,6,7,9],1)==[9,3,5,6,7,1]
  