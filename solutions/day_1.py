import time
import os
from collections import Counter


def historian_hysteria(list1, list2):
    list1.sort()
    list2.sort()
    start = time.time()
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    end = time.time()
    total_time = end - start
    return {"distance": distance, "time": total_time}

def historian_hysteria_solution2(list1, list2):
    list1.sort()
    list2.sort()
    start = time.time()
    distance = sum(abs(i - j) for i, j in zip(list1, list2))
    end = time.time()
    total_time = end - start
    return {"distance": distance, "time": total_time}


def similarity_score(list1, list2):
    list2_counts = Counter(list2)
    score = sum(num * list2_counts[num] for num in list1)
    return score


def load_data(file_path):
    list1, list2 = [], []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) == 2:
                list1.append(int(values[0]))
                list2.append(int(values[1]))
    return list1, list2


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "../data/input_day1.txt")
    list1, list2 = load_data(file_path)

    print("Using historian_hysteria:")
    print(historian_hysteria(list1, list2))
    print("Using historian_hysteria_solution2:")
    print(historian_hysteria_solution2(list1, list2))
    print("similarity score")
    print(similarity_score(list1,list2))
