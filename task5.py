# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть 
# всю последовательность (сдвиг - циклический) на |K| элементов вправо, если 
# K – положительное и влево, если отрицательное.
n=int(input('сколько чисел'))
list_1=list()
for i in range(n):
    list_1.append(int(input()))
k=int(input('насколько сдвинуть'))
list_2=[0]*n
print(list_1)
if k>0:
    for i in range(n): 
        b=(n-(i+k))*(-1)
        list_2[b]=list_1[i]
else:
    for i in range(n): 
        b=i+k
        list_2[b]=list_1[i]
print(list_2)