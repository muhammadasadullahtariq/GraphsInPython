import math
#Program That transfer message from one to all Process in hypercupe
source = []
destination = []
process = 0


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
    process = int(input("Enter Number of Process in power 2"))
    while(not isPowerOfTwo(process)):
        process = int(input("Enter Again Number of Process in power 2"))

def algorithum():
    #it always start from process 0 if you want to start from any other process than get node from user and place it instead of zero
    source.append(0)
    print(process)
    totalIteration = process//2
    print(totalIteration)
    divisier = 2
    i = 0
    while (len(source) < process):
        for j in range(len(source)):
            k = process//divisier
            destination.append(source[j]+k)# if you getting start process from user than replace source[j]+k with (source[j]+k)%p
        print(str(i) + "\tIteration :")
        i=i+1
        print("Source:\t" + str(source))
        print("Destination:\t" + str(destination))
        for j in range(len(destination)):
            source.append(destination[j])
        divisier = divisier*2
        destination.clear()
    print("At The End Source:\t" + str(source))
getNumberOfProcess()
algorithum()