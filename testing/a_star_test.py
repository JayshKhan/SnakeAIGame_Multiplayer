import heapq


def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def get_neighbors(pos, obstacles):
    neighbors = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible moves (Right, Left, Down, Up)

    for move in moves:
        neighbor = (pos[0] + move[0], pos[1] + move[1])
        if neighbor not in obstacles:
            neighbors.append(neighbor)

    return neighbors


def a_star(start, goal, obstacles):
    global current_pos
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current_pos = heapq.heappop(frontier)
        print(f"current_pos: {current_pos}")
        print(f"current_cost: {current_cost}")
        if current_pos == goal:
            print("Found goal")
            print(f"came_from: {came_from}")
            break

        for next_pos in get_neighbors(current_pos, obstacles):
            new_cost = cost_so_far[current_pos] + 1

            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost + heuristic(next_pos, goal)
                heapq.heappush(frontier, (priority, next_pos))
                came_from[next_pos] = current_pos

    # Reconstruct path
    path = []
    while current_pos != start:
        path.append(current_pos)
        current_pos = came_from[current_pos]

    # Determine the next direction
    next_pos = path[-2]
    dx, dy = next_pos[0] - start[0], next_pos[1] - start[1]

    if dx == 1:
        return "Right"
    elif dx == -1:
        return "Left"
    elif dy == 1:
        return "Down"
    elif dy == -1:
        return "Up"




if __name__ == "__main__":
    # Example usage
    snake_location = [(2, 2), (2, 3), (2, 4)]
    food_location = (7, 7)
    obstacle_locations = [(5, 5), (6, 5), (7, 5)]

    direction = a_star(snake_location[0], food_location, obstacle_locations)
    print("Next Direction:", direction)
