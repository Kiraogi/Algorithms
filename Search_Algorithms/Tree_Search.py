"""
Поиск по дереву — это название для различных алгоритмов, использующих структуру данных "дерево", чтобы эффективно
находить значения или узлы. Два основных типа поиска по дереву — это поиск в глубину (Depth-First Search, DFS)
и поиск в ширину (Breadth-First Search, BFS).

Поиск в глубину (DFS)
DFS исследует дерево, идя как можно глубже вдоль каждой ветви перед тем, как отступить.
Это может быть реализовано с помощью стека или рекурсии.

Пример рекурсивного DFS в бинарном дереве:
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    # Продолжаем поиск в поддеревьях
    return dfs(root.left, target) or dfs(root.right, target)

# Пример использования
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7)))

target = 5
found = dfs(root, target)
print("Элемент найден" if found else "Элемент не найден")

"""
Поиск в ширину (BFS)
BFS исследует дерево уровень за уровнем, начиная с корня и переходя к узлам следующего уровня после того, 
как все узлы текущего уровня были исследованы. Обычно это делается с помощью очереди.

Пример BFS в бинарном дереве:
"""
from collections import deque

def bfs(root, target):
    if root is None:
        return False
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.value == target:
            return True
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return False

# Пример использования аналогичен примеру DFS

"""
Выбор между DFS и BFS зависит от структуры дерева и типа задачи. DFS может быть предпочтительнее для деревьев с 
большой шириной, тогда как BFS лучше подходит для поиска кратчайшего пути в деревьях с большой глубиной, поскольку он 
находит ответ, как только достигает цели на минимально возможном уровне.
"""