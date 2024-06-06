"""
Сортировка вставками (Insertion Sort)
Сортировка вставками — это простой алгоритм сортировки, который строит отсортированный массив (или список) один элемент
за разом. Он работает по принципу выбора элемента из неотсортированной части массива и вставки его в правильную позицию
в уже отсортированной части.

Процесс сортировки вставками:

1) Начинаем с того, что считаем первый элемент массива отсортированным.
2) Берем следующий элемент и сканируем отсортированную часть массива справа налево.
3) Вставляем текущий элемент в правильную позицию в отсортированной части.
4) Повторяем шаги 2 и 3 до тех пор, пока все элементы не будут вставлены в отсортированную часть массива.

Сортировка вставками отличается стабильностью и хорошо работает на небольших массивах или на частично отсортированных
массивах, где требуется меньше перемещений.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы arr[0..i-1], которые больше, чем key,
        # на одну позицию вперед от их текущего места
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Пример использования
array = [4, 3, 2, 10, 12, 1, 5, 6]
insertion_sort(array)
print("Sorted array is:")
print(array)

"""
Временная сложность сортировки вставками в худшем случае составляет O(n^2), что делает ее менее эффективной для больших 
массивов по сравнению с более сложными алгоритмами, такими как быстрая сортировка, сортировка слиянием 
или пирамидальная сортировка. Тем не менее, для небольших или почти отсортированных массивов она может быть 
более быстрой и имеет преимущество в том, что легко реализуется и не требует дополнительной памяти.
"""
