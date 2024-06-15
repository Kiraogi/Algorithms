"""
Алгоритм сжатия данных Lempel-Ziv-Welch (LZW) является одним из наиболее известных алгоритмов сжатия без потерь.
Он широко использовался в форматах файлов, таких как GIF и TIFF, а также во многих других областях. Алгоритм LZW
основан на использовании словаря для замены повторяющихся последовательностей данных более короткими кодами.

Процесс работы LZW можно разделить на две основные стадии: сжатие и распаковка.

Сжатие (Кодирование)
1) Инициализация словаря с базовым набором символов (часто ASCII).
2) Поиск наибольшей строки W в словаре, которая соответствует текущей последовательности символов.
3) Вывод кода, соответствующего строке W.
4) Добавление W + следующего символа в словарь (расширение словаря).
5) Продолжение с шага 2 для оставшейся части данных.

Распаковка (Декодирование)
1) Чтение кода и вывод соответствующей строки из словаря.
2) Запоминание этой строки как последовательность W.
3) Чтение следующего кода и добавление W + первый символ следующей строки в словарь.
4) Вывод следующей строки.
5) Продолжение с шага 3.
"""

def lzw_compress(uncompressed):
    """Сжимает входную строку с помощью LZW."""
    # Строим словарь
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            # Выводим код для w
            result.append(dictionary[w])
            # Добавляем wc в словарь
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Выводим код для w
    if w:
        result.append(dictionary[w])
    return result


def lzw_decompress(compressed):
    """Распаковывает список целых чисел обратно в строку."""
    # Строим словарь
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    w = chr(compressed.pop(0))
    result = w
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)

        result += entry

        # Добавляем w+entry[0] в словарь
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result


# Пример использования
compressed = lzw_compress('TOBEORNOTTOBEORTOBEORNOT')
print(compressed)
decompressed = lzw_decompress(compressed)
print(decompressed)

"""
Обратите внимание, что этот пример представляет собой базовую реализацию и не оптимизирован для производительности или 
практического использования. Кроме того, в реальном сжатии LZW биты кода обычно упаковываются в байты, что требует 
дополнительной обработки для управления переменной длиной кодов.
"""