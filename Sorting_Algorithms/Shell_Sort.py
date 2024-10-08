"""
Сортировка Шелла — это обобщение сортировки вставками, которое позволяет сравнивать элементы, находящиеся на некотором
расстоянии друг от друга. Смысл заключается в том, чтобы сначала сортировать элементы, находящиеся на определённом
"шаге" друг от друга, а затем уменьшать шаг и сортировать снова. Этот метод значительно уменьшает общее
количество перемещений по сравнению с обычной сортировкой вставками.

Алгоритм:
Начать с большого значения шага (обычно шаг = половина длины массива), затем постепенно уменьшать шаг до 1.
На каждом шаге применять сортировку вставками для подмассивов, созданных на основе текущего шага.
Повторять процесс до тех пор, пока шаг не станет равным 1.

Пример:
Рассмотрим массив [12, 34, 54, 2, 3].

Шаг 1:
Шаг = 3 (половина длины массива).
Подмассивы: [12, 2], [34, 3], [54].
Сортируем каждый подмассив: [2, 12, 3, 34, 54].

Шаг 2:
Шаг = 1 (сортировка вставками для всего массива).
Проходим по массиву и сортируем его как при сортировке вставками.

Результат:
Итоговый массив: [2, 3, 12, 34, 54].
"""


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print(arr)

"""
Shell Sort эффективен для относительно небольших массивов и прост в реализации.

Преимущества:
* Быстрее, чем пузырьковая и вставками для больших массивов.
* Легко реализуется.

Недостатки:
* Сложно анализировать теоретическую производительность.
* Хуже, чем O(n log n) для больших массивов.
"""