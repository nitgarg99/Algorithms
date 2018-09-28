
def maxRegionUtil(grid, i, j, visited)
    visited[i][j] = 1
    count = 1

    if i > 0:
        if grid[i-1][j] and not visited[i-1][j]:
            count += maxRegionUtil(grid, i-1, j, visited)
    if i < len(grid):
        if grid[i+1][j] and not visited[i+1][j]:
            count += maxRegionUtil(grid, i+1, j, visited)
    if j > 0:
        if grid[i][j-1] and not visited[i][j-1]:
            count += maxRegionUtil(grid, i, j-1, visited)
    if j < len(grid):
        if grid[i][j+1] and not visited[i][j+1]:
            count += maxRegionUtil(grid, i, j-+, visited)

    return count

    
def maxRegion (grid):
    regionSizes = []
    visited = [[0 for j in range(len(grid[i])] for i in range(len(grid))]
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            if grid[i][j] and not visited[i][j]:
                count = 0 
                regionSizes.append(maxRegionUtil(grid, i, j, visited))

    return max(regionSizes)

n = int(input())
m = int(input())

grid = []
for _ in range n:
    grid.append(list(map(input().strip().split())))
