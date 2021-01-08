# task4
'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
import random

def check_fun(*args):
    for count, element in enumerate(args[0]):
        yield element

original_list = [element for element in range(random.randint(1, 10))]
add_list = [element for element in range(random.randint(1, 10))]
original_list.extend(add_list)
random.shuffle(original_list)
print(len(original_list), original_list)
add_number = check_fun(original_list)
print(add_number)
# for count, element in enumerate (original_list):
#     for number in original_list[count:]:
#         print (count, element)
#         if original_list.index(element, count) != 0:
#             print(f' попались {count}, {element}')
#             add_list.append(element)


print(add_list)