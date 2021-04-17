Graph = {
    "1": [["2",3], ["3",4]],
    "2": [["1",3], ["5",7], ["8",10], ["9",11]],
    "3": [["1",4], ["4", 7], ["6",9]],
    "4": [["3",7], ["5",9]],
    "5": [["4",9], ["2",7], ["6",11], ["8",13]],
    "6": [["3",9], ["5",11], ["7",13]],
    "7": [["6",13], ["8",15], ["11",18]],
    "8": [["2",10], ["5",13], ["7",15], ["11",19], ["12",20], ["10",18]],
    "9": [["2",11], ["10",19]],
    "10": [["8",18], ["9",19]],
    "11": [["8",19], ["7",18]],
    "12": [["8",20]]
}



print(Graph)

def minlol(lists):
    minValue = 999
    index = 0
    Mindex = -1
    while index < len(lists):
        lol = lists[index]
        if minValue > lol[1] :
            minValue = lol[1]
            Mindex = index
        index +=1
    return Mindex

def uniformsearch(Graph,startingN,goalN):
    listN = []
    backtrackStack = []
    visited = []
    path = []

    path.append([startingN,0])
    pathcost = 0
    print("Actual treverse :", end=" ")

    backtrackStack.append(startingN)
    while backtrackStack:
        listN.clear()
        Node = backtrackStack[-1]
        print(Node + "->", end="")
        visited.append(Node)
        if Node == goalN:

            print("\nsearching path  :", end=" ")
            for pathv in path:
                pathcost = pathv[1] + pathcost
                print(str(pathv[0]) + "->", end=" ")
            print("Goal Achived")
            print("Total path cost : " + str(pathcost))
            break

        for conectedNode in Graph[Node]:
            if conectedNode[0] not in visited and conectedNode[0] not in backtrackStack:
                listN.append(conectedNode)
        indexo = minlol(listN)
        if indexo != -1:
            adjN = listN[indexo]
            backtrackStack.append(adjN[0])
            path.append((listN[indexo]))
        else:
            backtrackStack.pop()



print("\nUniform cost Search :")
uniformsearch(Graph,"1","12")