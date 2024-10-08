"""
Сортировка слиянием (Merge Sort)
Сортировка слиянием также является алгоритмом "разделяй и властвуй".
Он разбивает массив на две половины, рекурсивно применяет сортировку слиянием к каждой половине, а затем сливает
отсортированные половины в один отсортированный массив.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Пример использования
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = merge_sort(array)
print(sorted_array)

"""
Преимущества:
* Стабильный (сохраняет порядок равных элементов).
* Хорошее и гарантированное время работы O(n log n).

Недостатки:
* Требует дополнительной памяти (O(n)).
* Медленнее на практике по сравнению с Quick Sort.
"""