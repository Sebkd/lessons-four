# task4
'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from random import randint, shuffle

original_list = [element for element in range(randint(1, randint(10, 15)))] + \
                [element for element in range(randint(1, randint(5, 10)))]
shuffle(original_list)
print(f'Original list = {original_list} \n'
      f'Changed list = {[el for el in original_list if original_list.count(el) == 1]} \n')