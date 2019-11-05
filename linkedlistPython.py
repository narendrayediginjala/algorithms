class Node:
  def __init__(self,value):
    self.value = value
    self.Next = None

class linked_list:
  def __init__(self):
    self.head=Node()
  def append(self,data):
    new_node = Node(data)
    curr = self.head
    while curr.Next!=None:
      curr = curr.Next
    curr.Next=new_node
  def length(self):
    total=0
    curr = self.head
    while curr.Next!=None:
      total+=1
      curr = curr.Next
    return total
  def display(self):
    elements = []
    curr = self.head
    while curr.Next!=None:
      elements = elements.append(curr.value)
      curr=curr.Next
    print(elements)
  def getItem(self,index):
    if index >= self.length or index<0:
      print("Error: Index out of range")
      return None
    curr_index = 0
    curr_node = self.head
    while True:
      if curr_index ==index:
        return curr_node.value
      curr_node = curr_node.Next
      curr_index+=1
    
