class Node:
  def __init__(self,data):
    self.data=data
    self.Next=None
class LinkedList:
  def __init__(self):
    self.head=None
    self.numOfNodes=0
  def insert(self,data):
    node=Node(data)
    if not self.head:
      self.head=node
l=LinkedList()
l.insert(10)