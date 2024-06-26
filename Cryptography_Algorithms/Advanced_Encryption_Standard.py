"""
Advanced Encryption Standard (AES) — это симметричный алгоритм блочного шифрования, который принят в качестве стандарта
шифрования правительством США и широко используется по всему миру. AES был введен в 2001 году после конкурса,
организованного Национальным институтом стандартов и технологий (NIST), и заменил старый стандарт
DES (Data Encryption Standard).

AES шифрует данные блоками по 128 бит, используя ключи фиксированной длины — 128, 192 или 256 бит.
Процедура шифрования состоит из нескольких раундов. Количество раундов зависит от длины ключа: 10 раундов для
128-битного ключа, 12 раундов для 192-битного ключа и 14 раундов для 256-битного ключа.

В каждом раунде выполняются следующие операции:
1) SubBytes: нелинейная подстановка, при которой каждый байт блока заменяется с использованием заранее определенной таблицы (S-box).
2) ShiftRows: циклический сдвиг строк блока.
3) MixColumns: смешивание данных внутри каждого столбца блока.
4) AddRoundKey: сложение с ключом раунда (каждый байт блока комбинируется с байтом ключа раунда с помощью операции XOR).

Перед первым раундом выполняется дополнительная операция AddRoundKey. Последний раунд немного отличается:
в нём нет шага MixColumns.

Дешифрование выполняется в обратном порядке с использованием обратных операций каждого шага.

Вот пример реализации шифрования и дешифрования с помощью AES в Python с использованием библиотеки PyCryptodome:
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Генерация случайного ключа
key = get_random_bytes(16)  # Для AES-128, для AES-192 или AES-256 используйте 24 или 32 байта соответственно.

# Создание шифра
cipher = AES.new(key, AES.MODE_CBC)

# Шифрование данных
plaintext = b"Secret Message"
padded_plaintext = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_plaintext)

# Сохраняем IV для дешифрования
iv = cipher.iv

# Дешифрование данных
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
padded_decrypted_text = cipher_decrypt.decrypt(ciphertext)
decrypted_text = unpad(padded_decrypted_text, AES.block_size)

print("Original text:", plaintext)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_text)

"""
Важно отметить, что AES требует, чтобы размер данных для шифрования был кратен размеру блока (128 бит или 16 байт). 
В примере используется функция pad, чтобы дополнить данные до необходимого размера. При дешифровании используется 
функция unpad, чтобы удалить дополнение.

Также стоит отметить, что при использовании AES в режиме CBC (Cipher Block Chaining) необходимо генерировать
и сохранять инициализирующий вектор (IV), который используется для шифрования первого блока данных. 
IV должен быть случайным и уникальным, но не обязательно секретным; обычно его передают вместе с зашифрованными данными.
"""