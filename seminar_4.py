import math
import os
from traceback import print_list
from unicodedata import name
from unittest import result
os.system("cls")

# №1. Вычислить число c заданной точностью d

# from math import pi
# number = 0.000000001
# print(pi / number)
# print(int(pi / number))
# print(int(pi / number) * number)
# print('pi->', int(pi / number) * number)

#############################################################


# № 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# num = int(input('Введите число '))


# def prime_factors(num):
#     while num % 2 == 0:  # для чётного числа
#         print(2, end=' ')
#         num = num/2

#     for i in range(2, int(math.sqrt(num))+1):  # для нечетного числа
#         while num % i == 0:
#             print(i, end=' ')
#             num = num/i
#     if num > 2:
#         print(num, end=' ')


# prime_factors(num)

#######################################################

# №3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

# import random

# num=int(input('Введите число '))
# my_list=[]
# for i in range(num):
#     my_list.append(random.randint(1,10))
# print(my_list)
# new_list=[]
# for i in my_list:
#     count=0
#     for x in my_list:
#         if x==i:
#             count+=1
#     new_list.append(count)
# no_duplicates=set()
# index=0
# while index<len(my_list):
#     if new_list[index]==1:
#         no_duplicates.add(my_list[index])
#     index+=1
# print(no_duplicates)

###########################################################

# №4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

def generate_superscript(x, n):
    if n == 0:
        return str(x)
    if n == 1:
        return str(x)+"x"
    superscript = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = str(x)
    if x != 0:
        result += "x**"
    for i in str(n):
        result += superscript[int(i)]
    return result

def generate_polynomial(k):
 
    result = []
    for i in range(k, -1, -1):
        coefficient = random.randint(0, 100)
        if coefficient != 0:
            result.append(generate_superscript(coefficient, i))
    return "+".join(result)
with open('result.txt','w') as res:
    res.write(generate_polynomial(10))
    res=(generate_polynomial(10))

print(res)

#############################################################

# №5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# with open('result_1.txt','w') as res:
#     res.write('33x**10+22x**9+39x**8+96x**7+47x**6+7x**5+6x**4+22x**3+38x**2+37x+98')

with open('result.txt','r') as file:
    o_1 = file.readline()
    l_1 = o_1.split()
with open('result_1.txt','r') as file:
    o_2 = file.readline()
    l_2 = o_2.split()
print(f'{l_1} + {l_2}')
sum_poly = l_1 + l_2
with open('sum_rez.txt', 'w') as file:
    file.write(f'{l_1} + {l_2}')