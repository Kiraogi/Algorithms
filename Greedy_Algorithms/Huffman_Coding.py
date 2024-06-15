"""
Алгоритм Хаффмана — это популярный метод сжатия данных без потерь. Он использует переменную длину кодирования для
представления символов; чем чаще символ встречается, тем короче будет его битовое представление. Основная идея алгоритма
Хаффмана заключается в построении оптимального бинарного дерева кодирования, где каждый лист дерева соответствует
символу из алфавита исходных данных.

Процесс кодирования Хаффмана состоит из нескольких этапов:
1) Подсчет частоты: Сначала алгоритм подсчитывает частоту каждого символа в исходных данных.
2) Создание листьев: Для каждого уникального символа создается лист дерева с частотой этого символа.
3) Построение дерева Хаффмана: Листья объединяются в бинарное дерево по следующему принципу:
    Выбираются два узла с наименьшей частотой.
    Создается новый узел с частотой, равной сумме частот выбранных узлов.
    Новый узел становится их родителем.
    Узлы с наименьшей частотой удаляются из списка, и новый узел добавляется в список.
    Процесс повторяется, пока в списке не останется только один узел, который станет корнем дерева Хаффмана.
4) Генерация кодов: Каждому символу присваивается уникальный код, соответствующий пути от корня дерева к соответствующему листу, где идти влево означает добавление бита 0, а идти вправо — бита 1.
5) Кодирование данных: Исходные данные кодируются путем замены каждого символа на его код Хаффмана.
6) Декодирование данных: Данные могут быть декодированы с помощью обратного процесса, используя построенное дерево Хаффмана.
"""
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Определяем сравнение для корректной работы heapq
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # Подсчет частоты каждого символа в тексте
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapify(heap)

    # Построение дерева Хаффмана
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush(heap, merged)

    return heap[0]  # Корень дерева


def huffman_coding(node, prefix="", code={}):
    # Рекурсивное создание кодов Хаффмана
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix
        huffman_coding(node.left, prefix + "0", code)
        huffman_coding(node.right, prefix + "1", code)
        return code


def encode(text, code):
    # Кодирование текста с использованием кодов Хаффмана
    return ''.join(code[char] for char in text)


def decode(encoded_text, root):
    # Декодирование текста с использованием дерева Хаффмана
    decoded_text = ""
    node = root
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_text += node.char
            node = root
    return decoded_text


# Пример использования
text = "this is an example for huffman encoding"
root = build_huffman_tree(text)
huffman_code = huffman_coding(root)
encoded_text = encode(text, huffman_code)
decoded_text = decode(encoded_text, root)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)

"""
В этом примере:
    Функция build_huffman_tree строит дерево Хаффмана на основе частоты символов в тексте.
    Функция huffman_coding рекурсивно генерирует коды Хаффмана для каждого символа.
    Функция encode преобразует исходный текст в закодированную строку, используя сгенерированные коды.
    Функция decode преобразует закодированную строку обратно в исходный текст, используя дерево Хаффмана.
Результатом работы алгоритма является закодированный текст, который обычно занимает меньше места, чем исходный, 
и который можно восстановить без потерь.
"""