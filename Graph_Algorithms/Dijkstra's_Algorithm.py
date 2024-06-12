"""
Алгоритм Дейкстры (Dijkstra's Algorithm) – это алгоритм на графах, который используется для нахождения кратчайшего
пути от одной из вершин графа до всех остальных. Алгоритм работает только с графами без отрицательных весов на ребрах.

Шаги алгоритма Дейкстры:
1) Инициализация: Установите начальную вершину в качестве текущей и расстояние от начальной вершины до нее равно 0,
а до всех остальных вершин бесконечность.
2) Обновление расстояний: Для текущей вершины пересчитайте расстояние до всех смежных вершин через текущую вершину.
Если новое расстояние до смежной вершины меньше текущего расстояния до нее, обновите расстояние.
3) Переход к следующей вершине: Пометьте текущую вершину как посещенную и выберите следующую вершину с наименьшим
расстоянием из непосещенных вершин в качестве новой текущей вершины.
4)Повторение: Повторяйте шаги 2 и 3, пока все вершины не будут посещены.
"""
import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Пример графа в виде словаря смежности
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1},
    'C': {'B': 1, 'A': 5}
}

# Вызов функции с начальной вершиной 'A'
start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print(shortest_distances)

"""
Алгоритм Дейкстры эффективно находит кратчайшие пути в графах без отрицательных весов на ребрах и 
может быть использован, например, для оптимизации маршрутов в сетях передачи данных или для нахождения 
кратчайшего пути в графе дорог.
"""
