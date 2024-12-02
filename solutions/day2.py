import os


def is_safe(levels):
    diff = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    for i in range(len(diff)):
        if (diff[0] > 0 > diff[i]) or (diff[0] < 0 < diff[i]):
            return False

    for i in range(len(diff)):
        if not (1 <= abs(diff[i]) <= 3):
            return False

    return True


def is_safe_with_removing(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    return False


def count(reports):
    safe_counter = 0
    for report in reports:
        if is_safe_with_removing(report):
            safe_counter += 1
    return safe_counter

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            data.append(levels)
    return data

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/input_day2.txt")
    reports= load_data(file_path)

    safe_count = count(reports)
    print(f"Number of safe reports: {safe_count}")
