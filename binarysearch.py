def binarysearch(l,r):
  si=len(l)//2
  found=False
  if si<=len(l) and len(l)>0:
    if l[si]==r:
      found=True
    elif l[si]<r:
      found=binarysearch(l[si+1:],r)
    else:
      found=binarysearch(l[:si],r)
  return found
if __name__=="__main__":
  assert binarysearch([1,3,5,6,7,9],5)==True
  assert binarysearch([1,3,5,6,7,9],10)==False
