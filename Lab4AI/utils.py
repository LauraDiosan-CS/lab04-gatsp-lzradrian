def readFromFile(fileName):
    matrix = []
    f = open(fileName, "r")
    nrNoduri = int(f.readline())
    for line in f:
        array = []
        currentline = line.split(",")
        for elem in currentline:
            array.append(float(elem))
        matrix.append(array)
    f.close()
    return matrix


from cmath import sqrt

def transform(filePath):
    problParam = {}
    nodes = [];
    nrNodes = 0;
    f = open(filePath, "r")
    while True:
        line = f.readline()
        # print("Linie!")
        if not line:
            break
        nrNodes += 1
        values = line.split(' ');
        a = float(values[1]);
        b = float(values[2]);
        nod = [a, b]
        nodes.append(nod)
    f.close();
    print("Am iesit!")
    ma = []
    for i in range(len(nodes)):
        line = []
        for j in range(len(nodes)):
            if i == j:
                line.append(0)
            else:
                # print((nodes[i][0]-nodes[j][0])*(nodes[i][0]-nodes[j][0]))
                # print(((nodes[i][1] - nodes[j][1])*(nodes[i][1] - nodes[j][1])))
                val = sqrt(((nodes[i][0] - nodes[j][0])*(nodes[i][0] - nodes[j][0])) + (nodes[i][1] - nodes[j][1])*(
                    nodes[i][1] - nodes[j][1])).real
                assert (val >= 0)
                line.append(val)
        ma.append(line)

    for i in range(len(nodes)):
        print(ma[i])

    problParam['noNodes'] = nrNodes
    problParam['mat'] = ma
    #return problParam
    return ma


#problParam = transform(filePath)