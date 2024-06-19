"""
Нейронные сети — это мощные вычислительные модели, вдохновленные структурой и функциями мозга, используемые для
решения разнообразных задач в области машинного обучения и искусственного интеллекта. Они состоят из большого количества
взаимосвязанных узлов, известных как искусственные нейроны, которые могут адаптировать свои веса в процессе обучения,
используя данные.

Нейронные сети обычно имеют три типа слоев:
1) Входной слой (Input layer): Принимает входные данные и передает их в сеть.
2) Скрытые слои (Hidden layers): Обрабатывают входные сигналы, преобразовывая их через веса, смещения и функции активации.
3) Выходной слой (Output layer): Генерирует окончательный вывод сети.

Процесс обучения нейронной сети включает в себя следующие этапы:
1) Прямое распространение (Forward propagation): Входные данные передаются через слои, в каждом из которых выполняются
взвешенные суммы и применяются функции активации, чтобы получить выходные данные.
2) Вычисление потерь (Loss calculation): Определение ошибки сети, сравнивая выходные данные сети с истинными значениями
с помощью функции потерь (например, среднеквадратическая ошибка).
3) Обратное распространение (Backpropagation): Вычисление градиентов функции потерь по отношению к весам и смещениям.
4) Оптимизация весов (Weight optimization): Обновление весов и смещений в направлении, уменьшающем потери, обычно
с использованием алгоритмов оптимизации, таких как стохастический градиентный спуск (SGD) или его варианты.

Одним из популярных фреймворков для работы с нейронными сетями в Python является TensorFlow, вот простой пример
создания и обучения нейронной сети с помощью Keras (высокоуровневый интерфейс для TensorFlow):
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Загрузка и предобработка набора данных MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28 * 28)).astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28)).astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Создание модели нейронной сети
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(Dense(10, activation='softmax'))

# Компиляция модели
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(train_images, train_labels, epochs=5, batch_size=128)

# Оценка модели на тестовых данных
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc:.2f}')

"""
В этом примере используется двухслойная нейронная сеть с одним скрытым слоем, содержащим 512 нейронов, и выходным слоем 
для 10 классов рукописных цифр. Функция активации relu используется в скрытом слое, а softmax — в выходном слое для 
классификации. Модель компилируется с оптимизатором rmsprop и функцией потерь categorical_crossentropy, подходящей для 
многоклассовой классификации. Обучение проводится в течение 5 эпох с размером партии в 128 примеров. 
После обучения модель оценивается на тестовых данных, выводится точность классификации.
"""