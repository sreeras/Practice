def solveCrossword(grid, n, cities, starts):
    if len(cities) == 0:
        return True

    for pos,city in enumerate(cities):
        # print (city, cities)
        # printCrossword(grid, n)
        # print("\n")
        # print(starts)

        if willCityFitInThisRow(grid, n, city, starts):
            updatedList = updateCityInThisRow(grid, n, city, starts)
            taken_city = city
            taken_start = starts.pop(0)
            if solveCrossword(grid, n, cities[:pos]+cities[pos+1:], starts):
                return True

            rollback(grid, n, updatedList, taken_start)

        if willCityFitInThisCol(grid, n, city, starts):
            updatedList = updateCityInThisCol(grid, n, city, starts)
            taken_city = city
            taken_start = starts.pop(0)
            if solveCrossword(grid, n, cities[:pos]+cities[pos+1:], starts):
                return True

            rollback(grid, n, updatedList, taken_start)

    return False


def computeStarts(grid, n):
    starts = []
    for i in range(n):
        for j in range(n):
            if isStart(grid, n, i, j):
                starts.append((i, j))
    return starts


def isStart(grid, n, i, j):
    if isFreeSlot(grid, n, i, j):
        # if top is blocked and bottom is not blocked then it is a start position
        if (((j - 1) >= 0 and grid[i][j - 1] == '+') or (j - 1 < 0)) and (j + 1) < n and isFreeSlot(grid, n, i, j + 1):
            return True

        # if left is blocked and right is not blocked then it is a start position
        if (((i - 1) >= 0 and grid[i - 1][j] == '+') or (i - 1 < 0)) and (i + 1) < n and isFreeSlot(grid, n, i + 1, j):
            return True
    return False


def willCityFitInThisRow(grid, n, city, starts):
    i, j = starts[0]
    for row in range(len(city)):
        if not isFreeSlot(grid, n, i, j + row):
            return False

    for row, s in enumerate(city):
        if 'A' <= grid[i][j + row] <= 'Z' and grid[i][j + row] != s:
            return False

    nextToLast = len(city) + j
    if nextToLast < n and isFreeSlot(grid, n, i, nextToLast):
        return False
    return True


def willCityFitInThisCol(grid, n, city, starts):
    i, j = starts[0]
    for col in range(len(city)):
        if not isFreeSlot(grid, n, i + col, j):
            return False

    for col, s in enumerate(city):
        if 'A' <= grid[i + col][j] <= 'Z' and grid[i + col][j] != s:
            return False

    nextToLast = len(city) + i
    if nextToLast < n and isFreeSlot(grid, n, nextToLast, j):
        return False
    return True


def updateCityInThisRow(grid, n, city, starts):
    updatedList = []

    i, j = starts[0]
    for row, s in enumerate(city):
        if grid[i][j + row] == '-':
            updatedList.append((i, j + row))
        grid[i][j + row] = s

    return updatedList


def updateCityInThisCol(grid, n, city, starts):
    updatedList = []
    i, j = starts[0]
    for col, s in enumerate(city):
        if grid[i + col][j] == '-':
            updatedList.append((i + col, j))
        grid[i + col][j] = s
    return updatedList


def isFreeSlot(grid, n, x, y):
    if 0 <= x < n and 0 <= y < n:
        if (grid[x][y] == '-') or ('A' <= grid[x][y] <= 'Z'):
            return True
    return False


def rollback(grid, n, updatedList, taken_start):
    i, j = updatedList[0]
    starts.insert(0, taken_start)

    for i, j in updatedList:
        grid[i][j] = '-'
    return True


def printCrossword(grid, n):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], sep='', end='')
        print()


n = int(input().strip())
# n = 10
grid = [['+'] * n for i in range(n)]

for i in range(n):
    grid[i] = list(input().strip())

cities = [city for city in input().strip().split(';')]

starts = computeStarts(grid, n)

# print(starts)
solveCrossword(grid, n, cities, starts)
# print(intersections)
printCrossword(grid, n)

