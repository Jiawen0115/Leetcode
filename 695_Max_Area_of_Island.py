#Question:  You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
#			You may assume all four edges of the grid are surrounded by water.
#			The area of an island is the number of cells with a value 1 in the island.
#			Return the maximum area of an island in grid. If there is no island, return 0.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = region_growing(grid,i,j,m,n)
                    max_area = area if area > max_area else max_area
        return max_area
                
def region_growing(grid,x,y,m,n)->int:
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    if grid[x][y] == 1:
        grid[x][y] = 0
        return 1+ sum([
        region_growing(grid,x-1,y,m,n),
        region_growing(grid,x+1,y,m,n),
        region_growing(grid,x,y+1,m,n),
        region_growing(grid,x,y-1,m,n)])
    else:
        return 0