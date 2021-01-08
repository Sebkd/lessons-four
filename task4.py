# task4
'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from random import randint, shuffle
from functools import reduce

def check_fun(*args):
    print(args)
    pass

original_list = [element for element in range(randint(1, 10))]
add_list = [element for element in range(randint(1, 10))]
original_list.extend(add_list)
shuffle(original_list)
print(original_list)
add_list.clear()
for count, element in enumerate(original_list, start = 1):
    add_list = list(filter(lambda number: number != element, original_list[count:]))
    print(count, element)
#add_list = [element for element in original_list if (filter(lambda number: number != element, original_list))]
print(add_list)

