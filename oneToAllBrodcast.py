import math

source = []
destination = []
p=0


def Log2(x):
    if x == 0:
        return False;
    return (math.log(x) /
            math.log10(2))
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)));
def getNumberOfProcess():
   p=int(input("Enter Number of Process in power 2"))
   while(not isPowerOfTwo(p)):
       p = int(input("Enter Again Number of Process in power 2"))
def algorithum():
    source.append(0);
    r = p/2
    d = 2
    for i in range(r):
        for j in range(len(source)):
            k = d/2
            destination.append(source[j]+k)
        for j in range(len(destination)):
            source.append(destination[j])
        d = d*2
        print(str(i) + "Iteration :")
        print("Source:"+source)
        print("Destination:"+destination)
        destination.clear()
getNumberOfProcess()
algorithum()