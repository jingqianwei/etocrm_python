#!/usr/bin/python
# -*- coding:utf8 -*-
# @TIME    : 2018/10/30 14:30
# @Author  : Chinwe
# @File    : Test.py

# age = 6

# if age >= 18:
# 	print('adult')
# elif age >= 6:
# 	print('teenager') 
# else:
# 	print('kid')

# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

# s = input('birth: ')
# birth = int(s) #转化为整型
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# names = [
# 	'Michael', 'Bob', 'Tracy'
# ]

# for name in names:
# 	print(name) # Michael, Bob, Tracy

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum) # 5050

# print(list(range(10)))  # [0,1,2,3,4,5,6,7,8,9]

# sum = 0
# n = 100
# while n > 0:
#     sum = sum + n
#     n = n - 1
# print(sum) # 5050

# n = 1
# while n <= 100:
# 	if n > 10: # 当n = 11时，条件满足，执行break语句
#         break  # break语句会结束当前循环
# 	print(n)
# 	n = n + 1
# print('END') # 1,2,3,4,5,6,7,8,9,10,END

# n = 0
# while n < 10:
# 	n = n + 1
# 	if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
# 	print(n) # 1,3,5,7,9

# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

# print(my_abs(-99)) # 99

# 类的基本用法
class Student(object):
    """docstring for Student"""

    def __init__(self, arg):
        self.arg = arg

    def get_grade(self):
        if self.arg >= 90:
            return 'A'
        elif self.arg >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student(90)
print(lisa.get_grade())  # A
