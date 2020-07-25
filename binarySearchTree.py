class Node:
  def __init__(self,data,parent):
    self.data=data
    self.leftChild=None
    self.rightChild=None
    self.parent=parent

class bst:
  def __init__(self):
    self.root=None

  def insert(self,data):
    if self.root is None:
      node = Node(data,None)
      self.root=node
    else:
      self.insert_node(data,self.root)

  def insert_node(self,data,node):
    if data <node.data:
      if node.leftChild:
        self.insert_node(data,node.leftChild)
      else:
        node.leftChild=Node(data,node)
    else:
      if node.rightChild:
        self.insert_node(data,node.rightChild)
      else:
        node.rightChild=Node(data,node)
  print("come to binarysearch tree program")
b = bst()
b.insert(30)
b.insert(55)