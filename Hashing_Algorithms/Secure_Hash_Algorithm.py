"""
Secure Hash Algorithm (SHA) — это семейство криптографических хеш-функций, которые разработаны и опубликованы
Национальным институтом стандартов и технологий (NIST) США. Они широко используются в различных приложениях
безопасности и целостности данных.

Существует несколько версий SHA, среди которых наиболее известны:
1) SHA-0: Оригинальный вариант, который позже был снят с учета из-за обнаруженных уязвимостей.
2) SHA-1: Производит 160-битное хеш-значение. Как и MD5, SHA-1 больше не считается безопасным для криптографического
использования из-за возможности нахождения коллизий.
3) SHA-2: Семейство, которое включает SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224 и SHA-512/256.
SHA-2 использует значительно большие размеры хешей и считается более безопасным. SHA-256 — это, пожалуй, самый часто
используемый вариант SHA-2.
4) SHA-3: Новейшее семейство стандартов, также известное как Keccak, победитель конкурса, проведенного NIST для замены
SHA-2. SHA-3 включает в себя такие функции, как SHA3-224, SHA3-256, SHA3-384 и SHA3-512.

Хеш-функции из семейства SHA используются для создания уникальных отпечатков данных и широко применяются в системах цифровых подписей, сертификации и других областях информационной безопасности.
"""
import hashlib


def calculate_sha256_hash(data):
    # Создаем объект SHA-256
    sha256_hash = hashlib.sha256()

    # Обновляем SHA-256-хеш данными
    sha256_hash.update(data.encode('utf-8'))

    # Получаем хеш в шестнадцатеричном формате
    digest = sha256_hash.hexdigest()
    return digest


# Пример использования
data = "Secure Hash Algorithm"
hash_result = calculate_sha256_hash(data)

print(f"SHA-256 hash of '{data}' is: {hash_result}")

"""
Этот код создает хеш SHA-256 для заданной строки и выводит его в шестнадцатеричном виде. 
SHA-256 считается надежным и широко используется для обеспечения целостности данных.
"""