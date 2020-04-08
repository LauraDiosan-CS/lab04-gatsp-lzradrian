from utils import readFromFile,transform
from Service import run

if __name__ == '__main__':
    print("Introduceti: \n 1 - pentru procesare easy.txt \n 2 - pentru procesare medium.txt \n 3 - pentru "
              "procesare hard.txt \n 4 - pentru procesare fricker26.txt \n 5 - pentru procesare berlin \n")

    ind = int(input())
    if (ind == 1):
        fileName = 'data/easy.txt'
    if (ind == 2):
        fileName = 'data/medium.txt'
    if (ind == 3):
       fileName = 'data/hard.txt'
    if (ind == 4):
        fileName = 'data/fricker26.txt'
    if (ind==5):
        filname = 'data/berlin.in'
        mat = transform('data/berlin.in')
    else:
        mat = readFromFile(fileName)

    problParam = {'matrix': mat, 'noNodes': len(mat)}
    generationParam = {'popSize': 400, 'noGen': 2000}

    run(problParam, generationParam)

