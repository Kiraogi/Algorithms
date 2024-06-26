"""
Message Digest Algorithm 5 (MD5) — это широко используемый хеш-алгоритм, который создает 128-битное (16-байтное)
хеш-значение, обычно представляемое как 32-значное шестнадцатеричное число. MD5 был разработан Рональдом Ривестом
в 1991 году и первоначально использовался в различных приложениях безопасности. Он также часто использовался для
проверки целостности данных.

Однако MD5 не считается надежным для использования в криптографических целях, поскольку были обнаружены серьезные
уязвимости, позволяющие находить коллизии — два разных входных сообщения, которые дают один и тот же MD5-хеш.
Это подрывает его использование для проверки подлинности и целостности данных, особенно в контексте безопасности.

Несмотря на уязвимости, MD5 все еще может использоваться для менее критичных задач, таких как создание уникальных
идентификаторов для наборов данных, где вероятность коллизий невелика.

"""
import hashlib


def calculate_md5_hash(data):
    # Создаем объект MD5
    md5_hash = hashlib.md5()

    # Обновляем MD5-хеш данными
    md5_hash.update(data.encode('utf-8'))

    # Получаем хеш в шестнадцатеричном формате
    digest = md5_hash.hexdigest()
    return digest


# Пример использования
data = "Hello World"
hash_result = calculate_md5_hash(data)

print(f"MD5 hash of '{data}' is: {hash_result}")

"""
Вышеприведенный код создает хеш MD5 для строки "Hello World" и выводит его в шестнадцатеричном виде. 
Имейте в виду, что использование MD5 для криптографических целей не рекомендуется, и для таких сценариев следует 
использовать более надежные алгоритмы, такие как SHA-256.
"""