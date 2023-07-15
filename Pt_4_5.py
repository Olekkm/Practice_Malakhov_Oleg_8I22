def allpath(current, end, graph, paths=[], path=[]):
    path += current
    if current == end:
        paths.append(path)
        return paths

    if graph.get(current) == ['']:
        return

    for i in graph.get(current):
        allpath(i, end, graph, paths, path[::1])

    return paths


def unique(arr):
    for i in arr:
        while arr.count(i) > 1:
            arr.remove(i)
    return arr


graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [''],
         'E': ['F'],
         'F': ['']}

for i in unique(allpath('A', 'F', graph)):
    print(i)
