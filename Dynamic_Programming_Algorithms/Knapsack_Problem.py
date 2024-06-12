"""
Задача о рюкзаке (Knapsack Problem) – это классическая задача комбинаторной оптимизации, которая заключается в выборе
определенных предметов с ограниченным вместимым весом, чтобы максимизировать их общую ценность или выгоду.

Существует два основных вида задачи о рюкзаке:
1) 0/1 задача о рюкзаке: В этой версии каждый предмет можно взять целиком или не взять вовсе
(то есть у нас нет возможности взять часть предмета). Цель – собрать набор предметов с максимальной общей ценностью,
не превышая общий вес рюкзака.
2) Непрерывная задача о рюкзаке: Здесь предметы можно брать частично (например, 0,1 кг от 3 кг),
поэтому решение может состоять из частей предметов. Цель – набрать предметы с максимальной общей ценностью,
уложившись в общий вес рюкзака.

Шаги решения задачи о рюкзаке:
1) Формулировка: Определите целевую функцию (например, максимизация общей ценности) и ограничения (вес рюкзака).
2) Динамическое программирование или жадные алгоритмы: Выберите подходящий метод для решения задачи в зависимости от
ее типа.
3) Реализация: Напишите код, который находит оптимальное решение задачи о рюкзаке.
"""


def knapsack_01(values, weights, max_weight):
    n = len(values)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    result = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]

    return dp[n][max_weight], result


# Пример использования
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50
max_value, items_selected = knapsack_01(values, weights, max_weight)
print("Максимальная общая ценность:", max_value)
print("Выбранные предметы:", items_selected)

"""
Задача о рюкзаке является важной в комбинаторной оптимизации и имеет много применений, например, в управлении запасами, 
финансовой аналитике, упаковке и многих других областях.
"""
