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
