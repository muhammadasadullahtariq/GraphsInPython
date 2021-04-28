import heapq

start,end,grid,row,column,heuristic,visited,distance=[],[],[],3,3,[],[],[]
def readFile():
    global column
    global row
    global start
    global end
    file = open("C:\\Users\Asad Ullah\Downloads\Compressed\grid.txt")
    column=int(file.read(3))
    row=int(file.read(3))
    print(row)
    print(column)
    for i in range(2):
        start.append(int(file.read(3)))
    z=[start[1],start[0]]
    start=z
    for i in range(2):
        end.append(int(file.read(3)))
    z=[end[1],end[0]]
    end=z
    for i in range(row):
        rowElement=[]
        j=0;
        while(j!=column):
            a=file.read(1)
            if(not (a=='\t' or a=='\n' or a==' ')):
                j=j+1
                a=int(a)
                rowElement.append(a)
        grid.append(rowElement)
    print(grid)
    print(start)
    print(end)
def mod(num):
    if(num<0):
        return num*-1;
    else:
        return num
def calculateHeursiticValue():
    global heuristic
    for i in range(row):
        var=[]

        for j in range(column):

            var.append(mod(i-end[0])+mod(j-end[1]))
        heuristic.append(var)
    print("Heuristic:")
    print(heuristic)
def findNeighbour(num):
    var=[]
    if(num[0]>row or num[1]>column):
        return var;
    if(column>1):
        if(num[1]+1<column and num[1]>0):
            var.append([num[0],num[1]+1])
            var.append([num[0],num[1]-1])
        elif(num[1]+1<column):
            var.append([num[0], num[1] + 1])
        else:
            var.append([num[0], num[1] - 1])
    if(row>1):
        if (num[0] + 1 < row and num[0] > 0):
            var.append([ num[0] + 1,num[1]])
            var.append([ num[0] - 1,num[1]])
        elif(num[0] + 1 < row):
            var.append([num[0] + 1, num[1]])
        else:
            var.append([num[0] - 1, num[1]])
    if(row>1):
        if(num[1]+1<column):
            if(num[0]>0 and num[0]+1<row):
                var.append([num[0]-1,num[1]+1])
                var.append([num[0]+1,num[1]+1])
            elif(num[0]>0):
                var.append([num[0]-1,num[1]+1])
            else:
                var.append([num[0] + 1, num[1] + 1])
        if (num[1] > 0):
            if (num[0] > 0 and num[0] + 1 < row):
                var.append([num[0] - 1, num[1] - 1])
                var.append([num[0] + 1, num[1] - 1])
            elif (num[0] > 0):
                var.append([num[0] - 1, num[1] - 1])
            else:
                var.append([num[0] + 1, num[1] - 1])
    return var

def GFSAlgo():
    global visited
    print(start)
    print(end)
    heapList = []
    heapq.heappush(heapList, (heuristic[start[0]][start[1]], start))
    while (heapq):
        node = heapq.heappop(heapList)
        print(node)
        print(visited)
        if (not (node[1] in visited)):
            visited.append(node[1])
            if (node[1] == end):
                break
            list = findNeighbour(node[1])
            print(list)
            while (list):
                if(grid[list[0][0]][list[0][1]]==0):
                    heapq.heappush(heapList, (heuristic[list[0][0]][list[0][1]], list[0]))
                list.pop(0)
    print("Visited")
    print(visited)

readFile()
calculateHeursiticValue()
GFSAlgo()

