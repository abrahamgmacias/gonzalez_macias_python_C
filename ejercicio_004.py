
# Funciones
def dotProduct(matrixOne, matrixTwo):
    matrixOneRows, matrixOneCols = len(matrixOne), len(matrixOne[0])
    matrixTwoRows, matrixTwoCols = len(matrixTwo), len(matrixTwo[0])
    emptyMatrix = [[0 for x in range(matrixTwoCols)] for y in range(matrixOneRows)]
    
    if matrixOneCols != matrixTwoRows:
        return "No se puede realizar el producto punto, las matrices son incompatibles"

    for row in range(matrixOneRows):
        for col in range(matrixTwoCols):
            for oneCol in range(matrixOneCols):
                emptyMatrix[row][col] += matrixOne[row][oneCol]*matrixTwo[oneCol][col]

    return tuple(tuple(row) for row in emptyMatrix)

# Variables
matrixA = ((1, 2, 3), (4, 5, 6))
matrixB = ((-1, 0), (0, 1), (1, 1))

# Resultados
print(dotProduct(matrixA, matrixB))

