"""
Алгоритм Краскала (Kruskal's Algorithm) – это алгоритм на графах, который используется для нахождения минимального
остовного дерева в связном взвешенном графе. Остовное дерево графа - это подграф, который является
деревом (не содержит циклов) и соединяет все вершины графа, используя наименьшее возможное количество ребер.

Шаги алгоритма Краскала:
1) Сортировка ребер: Отсортируйте все ребра графа по их весам.
2) Инициализация: Создайте пустой список для остовного дерева и наборы для каждой вершины графа.
3) Выбор ребра: Последовательно рассматривайте ребра в отсортированном порядке. Для каждого ребра:
    Если ребро соединяет две разные компоненты графа (т.е., добавление ребра не создает цикл),
    добавьте это ребро к остовному дереву и объедините две компоненты.
4) Повторение: Повторяйте шаг 3 до тех пор, пока не будет добавлено (V-1) ребер, где V - количество вершин в графе.
"""


class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_algorithm(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


# Пример использования алгоритма
g = Kruskal(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

min_spanning_tree = g.kruskal_algorithm()
print(min_spanning_tree)

"""
Алгоритм Краскала эффективно находит минимальное остовное дерево в графе и может быть использован, 
например, для оптимизации сетей передачи данных, планирования распределения ресурсов и многих других задач.
"""
