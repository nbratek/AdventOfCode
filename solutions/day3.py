import re
import os


def parse(memory):
    matches = re.findall(r"mul\([^)]+\)", memory)
    total_sum = 0
    for match in matches:
        try:
            args = match[4:-1].split(',')
            x, y = map(lambda num: int(num.strip()), args)
            total_sum += x * y
        except (ValueError, IndexError):
            continue

    return total_sum

def load_data(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/input_day3.txt")
    list1 = load_data(file_path)
    memory = " ".join(list1)
    result = parse(memory)
    print(f"The sum of the results of valid mul instructions is: {result}")
