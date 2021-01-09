# task1
'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

import argparse

parser = argparse.ArgumentParser (description = 'Скрипт расчета заработной платы сотрудника')
parser.add_argument ('production', type = int, help = 'Выроботка в часах на сотрудника, целое число')
parser.add_argument ('bid', type = float, help = 'Ставка в час на сотрудника, целое или дробное число')
parser.add_argument ('prize', type = float, help = 'Премия сотрудника, целое или дробное число')
args = parser.parse_args ()
print (f'Заработная плата сотрудника составляет: {args.production * args.bid + args.prize}')