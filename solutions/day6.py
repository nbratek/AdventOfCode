import os


def guard(map, start_row, start_col, start_direction, visited):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows, cols = len(map), len(map[0])
    row, col, direction = start_row, start_col, start_direction
    while 0 <= row < rows and 0 <= col < cols:
        visited[row][col] = True
        dr, dc = directions[direction]
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < rows and 0 <= next_col < cols and map[next_row][next_col] == "#":
            direction = (direction + 1) % 4
        else:
            row, col = next_row, next_col


def positions(map):
    marker = "^>v<"
    start_row, start_col, start_direction = None, None, None
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] in marker:
                start_direction = marker.index(map[row][col])
                start_row, start_col = row, col
                break
        if start_direction is not None:
            break
    rows, cols = len(map), len(map[0])
    visited = [[False] * cols for _ in range(rows)]
    guard(map, start_row, start_col, start_direction, visited)
    total_visited = 0
    for row in visited:
        for cell in row:
            total_visited += cell
    return total_visited


def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/input_day6.txt")
    map_data = load_data(file_path)
    result = positions(map_data)
    print(f"The guard visits {result} distinct positions.")

