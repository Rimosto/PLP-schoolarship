from collections import deque

# Sample maze (S=start, E=end, '#'=wall, ' '=open path)
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '#', ' ', ' ', ' ', 'E', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

def bfs_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)

    queue = deque([(start, [])])  # (current_position, path_taken)
    visited = set()

    while queue:
        (r, c), path = queue.popleft()
        if maze[r][c] == 'E':
            return path + [(r, c)]

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                maze[nr][nc] != '#' and (nr, nc) not in visited):
                queue.append(((nr, nc), path + [(r, c)]))
                visited.add((nr, nc))

    return []

path = bfs_maze(maze)
print("Shortest path:", path)