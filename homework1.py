###### Задача 2: Найдите сумму цифр трехзначного числа.

# number = int (input('Введите трёхзначное число: '))
# sum = 0 
# while number > 0:
#     remain = number % 10
#     sum += remain
#     number = number // 10
# print (sum)

# ______________________________________________________________________
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?


# s = int (input('Введите общее количество журавликов: '))
# pet = s//6
# ser = pet
# kat = (pet + ser)*2
# print (F"Петя сделал {pet} журавликов ,Катя сделала {kat} ,а Серёжа {ser} ")

# ______________________________________________________________________
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# .
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета

# number = input ('Enter the number of your ticket: ')
# if len(number) > 6 or len(number) < 6:
#     print ('YOU ENTERED THE WRONG NUMBER')
# else:
#     i = 0
#     index = len(number) // 2
#     sumleft = 0
#     sumright = 0
#     while i <= (len(number)//2 - 1):
#         sumleft = int (number[i]) +sumleft
#         i += 1
#     while index < len(number):
#         sumright = int (number[index]) + sumright
#         index += 1
#     print (sumleft)
#     print (sumright)
# if sumright == sumleft:
#     print ('Вы счастkивчик')
# else:
#     print('К сожалению билет не счастливый')


# ______________________________________________________________________
#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек, отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int (input('Введите количесво горизонтальных рядов шоколадки: '))
m = int (input('Введите количесво вертикальных рядов шоколадки: '))
k = int (input('Введите число сколько долек хотите отломить за раз '))
if k % n == 0 or  k % m == 0:
    print ("Можете смело отламывать")
else: print ("Ничего не выйдет!")