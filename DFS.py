graph = {1: [[2, 4], [3, 4]], 2: [[4, 5], [5, 5]], 3: [[6, 5], [7, 5]], 4: [[2, 5]], 5: [[2, 5]], 6: [[3, 5], [3, 5]],
         7: [[3, 5]]}


def limitCheck(limit, check):
    if (check < limit and check > 0):
        return True
    else:
        return False


def GatherGrapg():
    node = int(input("Enter Number of nodes:"))
    for i in range(1, node):
        list = []
        flag = True
        while (flag):
            opt = int(input("Enter Connected Node to " + str(i)))
            if (limitCheck(node, opt)):
                wei = int(input("Enter Weight:"))
                opti = []
                opti.append(opt)
                opti.append(wei)
                list.append(opti)
            else:
                flag = False
        graph[i] = list
def dfs(start):#enter starting node to traverse

    visted=[]
    queue=[]
    a=list(graph.keys())
    if (start in a):
        queue.append(start)
        while( queue):
            i=queue.pop()
            print(i)
            visted.append(i)
            edges=graph[i]
            for j in range(len(edges)):
                if(not (edges[j][0] in visted)):
                    queue.append(edges[j][0])

    print(visted)



dfs(1)
