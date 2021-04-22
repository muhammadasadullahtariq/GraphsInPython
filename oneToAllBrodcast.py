import math

source = []
destination = []
p = 0


def Log2(x):
    if x == 0:
        return False;
    return (math.log10(x) /
            math.log10(2))
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)));
def getNumberOfProcess():
    global p
    p = int(input("Enter Number of Process in power 2"))
    while(not isPowerOfTwo(p)):
        p = int(input("Enter Again Number of Process in power 2"))

def algorithum():
    source.append(0);
    print(p)
    r = p//2
    print(r)
    d = 2
    for i in range(r-1):
        for j in range(len(source)):
            k = p//d
            destination.append(source[j]+k)
        print(str(i) + "\tIteration :")
        print("Source:\t" + str(source))
        print("Destination:\t" + str(destination))
        for j in range(len(destination)):
            source.append(destination[j])
        d = d*2
        destination.clear()
    print("At The End Source:\t" + str(source))
getNumberOfProcess()
algorithum()