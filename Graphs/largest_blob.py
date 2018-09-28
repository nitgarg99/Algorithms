# Suppose you have a grid, and each square in the grid is a different color
# Colors next to eachother that are the same color form larger blobs
# Define a functio nthat will take this grid as an input and output the size
# of the largest blob

# Example -
# red, red, blue, blue
# red, red, red, green
# red, orange, blue, yellow

from collections import deque

def findBlobSize(grid, visited, i, j):

    visited.add((i, j))
    size = 0

    if i-1 >= 0: 
        if grid[i-1][j] == grid[i][j] and (i-1,j) not in visited:
            size += findBlobSize(grid, visited, i-1, j)
    if i+1 < len(grid):
        if grid[i+1][j] == grid[i][j] and (i+1,j) not in visited:
            size += findBlobSize(grid, visited, i+1, j)
    if j-1 < 0:
        if grid[i][j-1] == grid[i][j] and (i,j-1) not in visited:
            size += findBlobSize(grid, visited, i, j-1)
    if j+1 < len(grid[i]):
        if grid[i][j+1] == grid[i][j] and (i,j+1) not in visited:
            size += findBlobSize(grid, visited, i, j+1)

    size += 1

    return size


def maxBlobRecursive(grid):

    visited = set()
    max_blob = 0

    
    for i in range (0, len(grid)):
        for j in range(0, len(grid[i])):
            if (i,j) not in visited:
                blob_count = findBlobSize(grid, visited, i, j)
                if blob_count > max_blob:
                    max_blob = blob_count

    return max_blob

def visitNeighbors(grid, q, index, visited):
    i = index[0]
    j = index[1]
    neighbors = [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]
    for x,y in neighbors:
        boundaryCheck = x >= 0 and x < len(grid) and y >= 0 and y < len(grid)
        if boundaryCheck and (x,y) not in visited and grid[x][y] == grid[i][j]:
            q.appendleft((x,y))
            visited.add((x,y))
    return None

                      

def maxBlobIterative(grid):

    visited = set()
    q = deque()
    max_blob = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (i,j) not in visited:
                q.appendleft((i,j))
                visited.add((i,j))
                size = 0
                while q:
                    index = q.pop()
                    visitNeighbors(grid, q, index, visited)
                    size += 1
                if size > max_blob:
                    max_blob = size

    return max_blob

print(maxBlobRecursive([['r', 'r', 'b', 'b'], ['r', 'r', 'r', 'g'], ['r', 'o', 'b', 'b']]) )

print(maxBlobIterative([['r', 'r', 'b', 'b'], ['r', 'r', 'r', 'g'], ['r', 'o', 'b', 'b']]) )


    


