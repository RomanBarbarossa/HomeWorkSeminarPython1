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

number = input ('Enter the number of your ticket: ')
if len.number > 6 or len.number < 6:
    print ('YOU ENTERED THE WRONG NUMBER')
else:
    sumtotal = 0
    i = 0
    ind
    sumleft = 0
    sumright = 0
    while i < len(number)//2:
        sumleft = int (number[i]+sumleft)
        i += 1
    while ind < len(number):
        sumright = int (number[ind] + sumleft)
        ind += 1
    print (sumleft)
    print (sumright)
    print (sumleft +sumright)