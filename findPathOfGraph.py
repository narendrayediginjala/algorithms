graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def findPathOfGraph(graph,start,end,path=[]):
  path = path +[start]
  if start==end:
    return path
  if not start in graph.keys():
    return none
  for node in graph[start]:
    if node not in path:
      new_path=findPathOfGraph(graph,node,end,path)
      if new_path:return new_path
  return none

p=findPathOfGraph(graph,'A','D')
print(p)