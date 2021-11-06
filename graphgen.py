import random

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
def reset(i):
    i = 0


i = 0
maxVertex = 100
vertices = []
edges = []
while i < maxVertex:
    x = random.randint (1, 1000)
    y = random.randint (1, 1000)
    vertices.append(Vertex(i,x,y))
    i += 1
i = 0
while i < maxVertex - 1:
    edges.append(Edge(i,i+1))
    i += 1

i = 0
while i < (maxVertex*(maxVertex - 1))/2:
    x = random.randint(0,maxVertex)
    y = random.randint(0,maxVertex)
    if x != y:
        edges.append(Edge(x,y))
        i += 1
file = open("vertex2.txt","w") 
i = 0
while i < maxVertex:
    a = vertices[i].name
    b = vertices[i].x
    c = vertices[i].y
    string = str(a) + " " + str(b) + " " + str(c) + '\n'
    file.write(string)
    i += 1 
file.close()

file2 = open("edges2.txt","w") 
i = 0
while i < len(edges):
    a = edges[i].start
    b = edges[i].end
    string = str(a) + " " + str(b) + " " + '\n'
    file2.write(string)
    i += 1 
file2.close()

file3 = open("pairs2.txt","w") 
i = 0
while i < 35:
    a = random.randint(0,maxVertex)
    b = random.randint(0,maxVertex)
    string = str(a) + " " + str(b) + '\n'
    file3.write(string)
    i += 1 
file3.close()
