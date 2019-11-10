class Solution:
  def isValid(self, s):
    # Fill this in.
    l=[]
    flag = False
    for i in range(len(s)):
      if s[i]=='[':
        l.append('[')
      elif s[i]=='{':
        l.append('{')
      elif s[i]=='(':
        l.append('(')
      elif s[i]==']':
        l.remove('[')
      elif s[i]=='}':
        l.remove('{')
      elif s[i]==')':
        l.remove('(')
    if len(l)==0:
      flag=True
    return flag

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
