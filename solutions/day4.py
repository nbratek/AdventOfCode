import os


def search(grid, r, c, index, direction, word, rows, cols):
    word_len = len(word)
    if index == word_len:
        return 1
    nr, nc = r + direction[0], c + direction[1]
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[index]:
        return search(grid, nr, nc, index + 1, direction, word, rows, cols)
    return 0


def find_from_cell(grid, r, c, word, rows, cols):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    if grid[r][c] != word[0]:
        return 0
    total_count = 0
    for direction in directions:
        total_count += search(grid, r, c, 1, direction, word, rows, cols)
    return total_count


def count_xmas(grid, word):
    rows, cols = len(grid), len(grid[0])
    total_occurrences = sum(find_from_cell(grid, r, c, word, rows, cols) for r in range(rows) for c in range(cols))
    return total_occurrences


def load_grid(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/input_day4.txt")
    grid = load_grid(file_path)
    result = count_xmas(grid, "XMAS")
    print(f"The word 'XMAS' appears {result} times.")
