# Day 5: Recursion - Maze solver

def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def solve_maze(maze):
    n = len(maze)
    solution = [[0 for _ in range(n)] for _ in range(n)]

    def solve(x, y):
        if x == n - 1 and y == n - 1 and maze[x][y] == 1:
            solution[x][y] = 1
            return True

        if is_safe(maze, x, y):
            solution[x][y] = 1

            # Move down
            if solve(x + 1, y):
                return True
            # Move right
            if solve(x, y + 1):
                return True

            # Backtrack
            solution[x][y] = 0
            return False

        return False

    if solve(0, 0):
        for row in solution:
            print(row)
    else:
        print("No path found!")

# For example maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
