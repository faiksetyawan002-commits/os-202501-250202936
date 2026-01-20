import csv
import os

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request


def build_wait_for_graph(processes, allocation, request):
    graph = {p: [] for p in processes}

    for p1 in processes:
        for p2 in processes:
            if p1 != p2:
                # p1 menunggu resource yang sedang dipegang p2
                if request[p1] == allocation[p2]:
                    graph[p1].append(p2)

    return graph


def detect_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


def deadlock_processes(graph):
    """Mengambil proses yang berada dalam siklus"""
    deadlocked = set()
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        stack.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in stack:
                cycle_index = stack.index(neighbor)
                deadlocked.update(stack[cycle_index:])

        stack.pop()

    for node in graph:
        if node not in visited:
            dfs(node)

    return deadlocked


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_FILE = os.path.join(BASE_DIR, "dataset_deadlock.csv")

    processes, allocation, request = read_dataset(CSV_FILE)
    graph = build_wait_for_graph(processes, allocation, request)

    print("Wait-For Graph:")
    for k, v in graph.items():
        print(f"{k} -> {v}")

    if detect_cycle(graph):
        print("\nDEADLOCK TERDETEKSI!")
        print("Proses yang terlibat deadlock:")
        for p in deadlock_processes(graph):
            print("-", p)
    else:
        print("\nSistem dalam kondisi AMAN (tidak deadlock)")
