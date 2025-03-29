# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
"""" ● Пример вывода:
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3
    1 * 4 = 4
    1 * 5 = 5
    1 * 6 = 6
    ..
    1 * 9 = 9 """

import time

NUM = int(input("Enter your number(n): "))
LIM = int(input("Enter limit of table: "))
start = time.time()

def pythagoras_table_imperative():
    for b in range(1, LIM+1):
        print(f'{NUM:2} * {b:2} = {NUM*b:2}')
    print(f'Time elapsed: {time.time() - start}')


if __name__ == "__main__":
    pythagoras_table_imperative()

# Обоснование выбора парадигмы: структурная, процедурная
# код структурирован, последовательность его работы понятна, возможно переиспользование кода