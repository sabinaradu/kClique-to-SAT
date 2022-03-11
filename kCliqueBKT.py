import sys
import itertools


def readInput(inputFile):

    f = open(inputFile, "r")
    exp = ""

    for i in f:
        exp += i

    f.close()
    return exp


def verifyClique(graph, c):
    for i in c:
        ok = 0
        clique = i
        for u in clique:
            for v in clique:
                if graph[u - 1][v - 1] == 0 and u != v:
                    ok = 1
                    break;
        if ok == 0:
            return True


    return False



if __name__ == '__main__':
    inputFile = sys.argv[1]
    exp = readInput(inputFile)


    exp = exp.split('\n')
    k = int(exp[0])
    N = int(exp[1])
    M = int(exp[2])

    graph = [[0 for col in range(N)] for row in range (N)];
    vertex = [0 for x in range(N)]

    for i in range(N):
        vertex[i] = i + 1

    exp = exp[3:]
    for i in range(M):
        l = exp[0]
        l = l.split(" ")
        x = int (l[0])
        y = int (l[1])

        graph[x - 1][y - 1] = 1
        graph[y - 1][x - 1] = 1
        exp = exp[1:]


    # result = verifyClique(k, graph, vertex)
    # print(result)

    c = list(itertools.combinations(vertex, k))
    print(verifyClique(graph, c))

    # clique = []
    # clique = c[0]
    # print(clique)


    # for i in range(N):
    #     for j in range(N):
    #         print(graph[i][j])
    #     print("\n")
