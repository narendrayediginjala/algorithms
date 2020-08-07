class Solution(object):
  def canPick2(self, arr):
    # Fill this in.
    if len(arr)<5:
      return False
    else:
      start=1
      end=len(arr)-2
      part1sum=arr[0]
      part3sum=arr[end]
      flag=False
      while start<end and flag is not True:
        part2Sum=sum(arr[start+1:end])
        #print("start ",start)
        #print("end ",end)
        #print("part1sum ",part1sum)
        #print("part2sum ",part2Sum)
        #print("part3sum ",part3sum)
        if part1sum==part2Sum and part2Sum==part3sum:
          flag=True
        else:
          s1=part1sum
          s3=part3sum
          if part1sum<part3sum:
            s1=part1sum+arr[start]
            start+=1
          if part3sum<part1sum:
            s3=part3sum+arr[end]
            end-=1
          if part3sum==part1sum:
            s1=part1sum+arr[start]
            start+=1
            s3=part3sum+arr[end]
            end-=1
          part1sum=s1
          part3sum=s3

      return flag


assert(Solution().canPick2([2, 4, 5, 3, 3, 9, 2, 2, 2])==True)
# True

assert(Solution().canPick2([1, 2, 3, 4, 5])==False)
# False