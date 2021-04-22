import math
#Program That transfer message from one to all Process in Ring
source,destination,process=[],[],0
def Log2(x):
    if x == 0:
        return False;
    return (math.log10(x) /
            math.log10(2))
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)));
def getNumberOfProcess():
    global process
    process = int(input("Enter Number of Process in power 2 of Ring"))
    while(not isPowerOfTwo(process)):
        process = int(input("Enter Again Number of Process in power 2 of Ring"))

def algorithum():
    startNode=int(input("Enter Starting Node:"))
    while(not startNode<process):
        startNode = int(input("Enter Starting Node Again:"))
    source.append(startNode)
    diviser = 2
    i=0
    while(len(source)<process):
        for j in range(len(source)):
            k = process // diviser
            destination.append((source[j] + k)%process)
        print(str(i) + "\tIteration :")
        i=i+1;
        print("Source:\t" + str(source))
        print("Destination:\t" + str(destination))
        for j in range(len(destination)):
            source.append(destination[j])
        diviser = diviser * 2
        destination.clear()
    print("At The End Source:\t" + str(source))
getNumberOfProcess()
algorithum()