graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def findPathOfGraph(graph,start,end,path=[]):
  path = path +[start]
  if start==end:
    return [path]
  if not start in graph.keys():
    return none
    path = []
  for node in graph[start]:
    if node not in path:
      new_path=findPathOfGraph(graph,node,end,path)
      if new_path:return new_path
  return none

def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if not start in graph.keys():
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths

def find_shortest_paths(graph,start,end,path=[]):
  path = path+[start]
  if start==end:
    return path
  if not start in graph.keys():
    return None
  shortestpath=None
  for node in graph[start]:
    if node not in path:
      newpath = find_shortest_paths(graph,node,end,path)
      if newpath:
        if (not shortestpath) or (len(newpath)<len(shortestpath)):
          shortestpath=newpath
  return shortestpath


p=findPathOfGraph(graph,'A','D')
print("first path found=",p)

np=find_all_paths(graph,'A','D')
print("all paths=",np)

sp=find_shortest_paths(graph,'A','D')
print("shortest path=",sp)