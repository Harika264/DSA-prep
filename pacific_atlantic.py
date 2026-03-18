def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prev):
        if (r,c) in visited or r<0 or c<0 or r>=rows or c>=cols or heights[r][c] < prev:
            return
        visited.add((r,c))
        dfs(r+1,c,visited,heights[r][c])
        dfs(r-1,c,visited,heights[r][c])
        dfs(r,c+1,visited,heights[r][c])
        dfs(r,c-1,visited,heights[r][c])

    for i in range(rows):
        dfs(i,0,pac,heights[i][0])
        dfs(i,cols-1,atl,heights[i][cols-1])

    for j in range(cols):
        dfs(0,j,pac,heights[0][j])
        dfs(rows-1,j,atl,heights[rows-1][j])

    return list(pac & atl)
