"""
Быстрая сортировка (Quick Sort)
Быстрая сортировка — это эффективный алгоритм сортировки, использующий стратегию "разделяй и властвуй".
Алгоритм выбирает элемент из массива, который называется опорным (pivot), и разделяет массив на две части:
элементы меньше опорного и элементы больше или равные опорному.
Затем он рекурсивно применяет ту же стратегию к обеим частям.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array)
print(sorted_array)
