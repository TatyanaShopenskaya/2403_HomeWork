# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
#и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def degree(a,b):
    for i in range(a):
        if b == 0:
            return 1
        else:
            return a*degree(a,b-1)       #так же возвести в степень можно так - (return a**b)2
        
a = int(input('Введите число A - '))
b = int(input('Введите число B - '))

print(degree(a,b))