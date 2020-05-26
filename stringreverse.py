def reversestring(str):
  mi = len(str)//2
  firsthalf=""
  secondhalf=""
  for i in range(mi):
    firsthalf = firsthalf+str[len(str)-i-1]
    secondhalf=str[i]+secondhalf
  if len(str)%2!=0:
    firsthalf=firsthalf+str[mi]
  return firsthalf+secondhalf
if __name__=="__main__":
  assert reversestring("teststring")=="gnirtstset"
  assert reversestring("something")=="gnihtemos"
