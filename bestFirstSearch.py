import heapq

class breathFirstSearch:
    def __init__(self):
        self.graph = {'a': [['b', 11], ['c', 14], ['d', 7]],
                      'b': [['a', 11], ['e', 15]],
                      'c': [['a', 14], ['e', 8], ['f', 10]],
                      'd': [['a', 7], ['f', 25]],
                      'e': [['b', 15], ['h',9]],
                      'f': [['g', 20], ['d', 25]],
                      'g': [['f', 20], ['h', 10]],
                      'h': [['e', 9], ['g', 10]]}
        self.Heuristic={'a':40,
                        'b':32,
                        'c':25,
                        'd':35,
                        'e':19,
                        'f':17,
                        'h':10,
                        'g':0}
        self.node=0
        self.goal='g'
        self.visited=[]
    def checkLimit(self,a):
        if(a<self.node):
            return  True
        else:
            return False
    def gatherData(self):
        self.node=input("Enter total nodes(In char):")
        self.node=chr(ord(self.node)+1)
        for i in range(ord("a"),ord(self.node)):
            connectedNode = []
            while(True):
                connected = input("Enter connected node:" + chr(i))
                if(self.checkLimit(connected)):
                    weight=int(input("Enter Weight of node:"))
                    edge=[]
                    edge.append(connected)
                    edge.append(weight)
                    connectedNode.append(edge)
                else:
                    self.graph[chr(i)]=connectedNode
                    break
    def getGoal(self):
        while(True):
            goal=input("Enter Goal:")
            if(self.checkLimit(goal)):
                break

    def algo(self,starting):
        heapList = []
        heapq.heappush(heapList,(self.Heuristic[starting],starting))
        while(heapq):
            node = heapq.heappop(heapList)
            if(not (node[1] in self.visited)):
                self.visited.append(node)
                if(node[1]==self.goal):
                    break
                list=self.graph[node[1]].copy()
                while(list):
                    heapq.heappush(heapList,(self.Heuristic[list[0][0]],list[0][0]))
                    list.pop(0)
        print(self.visited)

    def calculateCost(self,visit):
        pathCost=0;
        for i in range(0,len(visit)-1):
            list=self.graph[visit[i]]
            while (list):
                a = list.pop(0)
                if (a[0] == visit[i+1]):
                    pathCost+=a[1]
        return pathCost

    def path(self):
        visit=[]
        while(self.visited):
            visit.append(self.visited[0][1])
            self.visited.pop(0)
        print(visit)
        print("Total Cost is "+str(self.calculateCost(visit)))



b=breathFirstSearch()
b.algo('a')
b.path()
