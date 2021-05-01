file =open("output.txt","w")

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

readFile()
def WriteFile():
    for i in range(row):
        for j in range(column):
            file.write(str(grid[i][j])+"\t")
        file.write("\n");
WriteFile()