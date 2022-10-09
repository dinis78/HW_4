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
    superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    result = str(x)
    if x != 0:
        result += "x"
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

res=str(generate_polynomial(10))

print(res)
   #with open('result.txt','a') as res: