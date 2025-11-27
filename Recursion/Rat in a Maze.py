def is_safe(x, y, maze, n, visited):
    # Check if (x,y) is within bounds, open (1), and not yet visited
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]


def solve_maze_util(x, y, maze, n, visited, path, result):
    # If destination is reached
    if x == n - 1 and y == n - 1:
        result.append("".join(path))
        return

    # Mark current cell as visited
    visited[x][y] = True

    # Possible directions: Down, Left, Right, Up
    directions = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]

    for dx, dy, move in directions:
        new_x, new_y = x + dx, y + dy
        if is_safe(new_x, new_y, maze, n, visited):
            path.append(move)
            solve_maze_util(new_x, new_y, maze, n, visited, path, result)
            path.pop()  # Backtrack

    # Unmark current cell
    visited[x][y] = False


def solve_maze(maze):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    result = []

    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []  # No path if start or end is blocked

    solve_maze_util(0, 0, maze, n, visited, [], result)
    return result


# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    paths = solve_maze(maze)
    if paths:
        print("Possible paths are:")
        for p in paths:
            print(p)
    else:
        print("No path exists")
