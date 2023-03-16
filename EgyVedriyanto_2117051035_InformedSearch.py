# Import libraries
from queue import PriorityQueue

# Define function to find the position of the blank tile (represented by 0)
def find_blank_tile(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == 0:
                return i, j

# Define heuristic function (Manhattan distance)
def heuristic(puzzle, goal):
    h = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] != goal[i][j]:
                x, y = find_blank_tile(goal)
                h += abs(i-x) + abs(j-y)
    return h

# Define A* algorithm function
def astar(puzzle, goal):
    pq = PriorityQueue()
    pq.put((0, puzzle, []))
    visited = set()

    while not pq.empty():
        (f, state, path) = pq.get()

        if state == goal:
            return path

        if str(state) in visited:
            continue

        visited.add(str(state))

        x, y = find_blank_tile(state)

        if x > 0:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
            new_path = path + ['U']
            pq.put((f + heuristic(new_state, goal), new_state, new_path))

        if x < len(puzzle)-1:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
            new_path = path + ['D']
            pq.put((f + heuristic(new_state, goal), new_state, new_path))

        if y > 0:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
            new_path = path + ['L']
            pq.put((f + heuristic(new_state, goal), new_state, new_path))

        if y < len(puzzle)-1:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
            new_path = path + ['R']
            pq.put((f + heuristic(new_state, goal), new_state, new_path))

    return None

# Define initial and goal states
puzzle = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Call A* algorithm function and print result
result = astar(puzzle, goal)
print(result)
