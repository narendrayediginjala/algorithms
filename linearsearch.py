def linearsearch(l,x):
	found = False
	for i in range(len(l)):
		if l[i]==x:
			found = True
			break
	return found
