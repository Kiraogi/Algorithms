"""
Алгоритм RSA (Rivest–Shamir–Adleman) — это криптографический алгоритм с открытым ключом, который используется для
защиты данных. Он основан на математической трудности задачи факторизации больших чисел. Алгоритм RSA может
использоваться для шифрования данных и для создания цифровых подписей.

Процесс использования RSA состоит из трех основных шагов: генерация ключей, шифрование и дешифрование.

Генерация ключей
1) Выбрать два больших простых числа p и q.
2) Вычислить n = p * q. Число n будет использоваться как модуль для обоих ключей.
3) Вычислить значение функции Эйлера от n: φ(n) = (p-1) * (q-1).
4) Выбрать целое число e, такое что 1 < e < φ(n) и e взаимно просто с φ(n). Часто используют стандартные значения,
например, 65537.
5) Вычислить d такое, что d * e mod φ(n) = 1. Число d является мультипликативно обратным к e по модулю φ(n).

Публичный ключ — это пара (e, n), а приватный ключ — это (d, n).

Шифрование
Чтобы зашифровать сообщение m, получатель должен использовать публичный ключ отправителя и вычислить шифртекст c так:
c = m^e mod n

Дешифрование
Чтобы расшифровать шифртекст c, получатель должен использовать свой приватный ключ и вычислить исходное сообщение m так:
m = c^d mod n

Вот пример реализации RSA на Python, используя библиотеку Crypto для генерации простых чисел и вычисления обратных
элементов:
"""
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse


def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def rsa_encrypt(public_key, plaintext):
    key = RSA.import_key(public_key)
    plaintext_bytes = plaintext.encode('utf-8')
    encrypted_msg = pow(int.from_bytes(plaintext_bytes, byteorder='big'), key.e, key.n)
    return encrypted_msg


def rsa_decrypt(private_key, encrypted_msg):
    key = RSA.import_key(private_key)
    decrypted_msg = pow(encrypted_msg, key.d, key.n)
    return decrypted_msg.to_bytes((decrypted_msg.bit_length() + 7) // 8, byteorder='big').decode('utf-8')


# Пример использования
private_key, public_key = generate_rsa_keys()
message = "Secret message"
encrypted = rsa_encrypt(public_key, message)
print("Encrypted:", encrypted)
decrypted = rsa_decrypt(private_key, encrypted)
print("Decrypted:", decrypted)

"""
Этот пример не предназначен для использования в реальных приложениях, т.к. он не включает важные практики безопасности, 
такие как использование криптографически безопасной схемы шифрования с открытым ключом (например, OAEP) и не 
обрабатывает возможные ошибки.
"""
