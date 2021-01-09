# task6
'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''
from itertools import count, cycle
import argparse

def counter(start, end):
    for number in count(start):
        if number > end:
            break
        else:
            yield number

def repeater(line, end):
    for i, value in enumerate(cycle(line)):
       if i > (end * len(line) - 1):
           break
       else:
           yield value

parser = argparse.ArgumentParser (description = 'Скрипт для итератора, генерирующего целые числа, начиная с указанного'
                                                '\n и Скрипт итератор, повторяющий элементы некоторого списка,'
                                                ' определенного заранее.')
parser.add_argument ('start_number', type = int, help = 'начальное значение генератора, целое число')
parser.add_argument ('end_number', type = int, help = 'конечное значение генератора, целое число')
parser.add_argument ('end_number_2', type = int, help = 'конечное значение повторяющего генератора, целое число')
parser.add_argument ('work_list', type = str, help = 'Строка списка, введите значение в кавычках " "')
args = parser.parse_args ()
print (f'Введеные данные: {args.start_number}, {args.end_number}, {args.end_number_2}, {args.work_list} ')
list_generator = counter(args.start_number, args.end_number)
my_list = [el for el in list_generator]
list_generator_2 = repeater(args.work_list, args.end_number_2)
my_list_2 = ''.join(list(el for el in list_generator_2))
print(f'Итератор, генерирующий целые числа, начиная с указанного и до указанного:\n{my_list}'
      f'\nИтератор, повторяющий элементы списка "{args.work_list}":\n{my_list_2}', end = ' ')
