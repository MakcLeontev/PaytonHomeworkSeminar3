# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list_1=[1.1, 1.2, 3.1, 5, 10.01]
list_2=list()
for i in range(len(list_1)):
    list_2.append(list_1[i]%1)
print(max(list_2)-min(list_2))
