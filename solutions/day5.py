import os


def calculate(rules, updates):
    total_sum = 0
    for update in updates:
        relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
        if is_correct(update, relevant_rules):
            total_sum += update[len(update) // 2]
    return total_sum


def is_correct(update, rules):
    seen = set()
    for page in update:
        for x, y in rules:
            if y == page and x not in seen:
                return False
        seen.add(page)
    return True

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    rules_section, updates_section = data.split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    return rules, updates


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/input_day5.txt")
    rules, updates = load_data(file_path)
    result = calculate(rules, updates)
    print(f"The sum: {result}")
