def binarysearch(l,x):
	si = len(l)//2
	found = False
	if si>=0 and si<len(l):
		if l[si]==x:
			found = True
		elif l[si]>x:
			found=binarysearch(l[:si],x)
		else:
			found=binarysearch(l[si+1:],x)
	return found
