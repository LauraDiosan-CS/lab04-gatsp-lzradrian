from GA import GA


def run(probParam=None, generationParam=None):
    probParam['function'] = CalculateFitness
    runGenerations(probParam, generationParam)


def runGenerations(probParam=None, generationParam=None):
    #star genetic algorithm
    ga = GA(generationParam, probParam)
    ga.initialisation()
    ga.evaluation()

    #run generations
    g = -1
    while (g < generationParam['noGen']):
        g += 1
        # ga.oneGenerationRand()
        ga.oneGenerationElitism()
        # ga.oneGenerationSteedyState()
        #print best fitness of current generation
        print("Generatia curenta: " + str(g) + "; " + "Best fitness: " + str(ga.bestChromosome().fitness))

    #print other parameters
    cost = int(ga.bestChromosome().fitness)
    path = ga.bestChromosome().repres
    strpath = ''

    path.insert(0, 0)
    for i in range(len(path)):
        strpath += str(path[i] + 1)
        if i != len(path) - 1:
            strpath += ','
    print("Lungimea traseului: " + str(len(path)))
    print("Traseu: " + strpath)
    print("Cost: " + str(cost))



def CalculateFitness(path, probParam):
    '''
    Calcularea fitness-ului
    :param probParam: matrix
    :return: float - fitness
    '''
    matirx = probParam['matrix'];
    fit = 0.0
    i = 0;
    for j in range(len(path)):
        fit += matirx[i][path[j]];
        i = path[j];
    fit += matirx[i][0];
    return fit
