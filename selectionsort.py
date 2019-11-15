def selectionsort(l):
  for i in range(len(l)):
    curr=i
    for j in range(i+1,len(l)):
      if l[curr]>l[j]:
        curr=j
    l[i],l[curr]=l[curr],l[i]
  return l
print("input:",[64, 25, 12, 22, 11] )
print("sorted list:",selectionsort([64, 25, 12, 22, 11] ))
