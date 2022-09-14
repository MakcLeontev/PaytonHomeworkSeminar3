# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
list_1=[2, 3, 4, 5, 6]
list_2=list()
if len(list_1)%2==0:
    for i in range(int(len(list_1)/2)):
        list_2.append(list_1[i]*list_1[len(list_1)-i-1])
else:
    for i in range(int(len(list_1)/2+1)):
        list_2.append(list_1[i]*list_1[len(list_1)-i-1])
print(list_2)    
