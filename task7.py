# task7
'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''
from math import factorial
from random import randint

def fact(end_number):
    for el in range(1, end_number+1):
        print(f'Факториал {el}! = {factorial(el)}')
    yield factorial(end_number)

calc_number = randint(1,25)
get_fact = fact(calc_number)
print(f'\nЧисло n = {calc_number}, Факториал n! = {[el for el in get_fact]}, Проверка = {factorial(calc_number)}')