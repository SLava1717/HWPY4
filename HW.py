 
#Задана натуральная степень k. Сформировать случайным образом список \
 #коэффициентов (значения от -100 до 100) многочлена и записать в файл \
 #многочлен степени k. 
#Пример:
 #k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.


from random import randint
 
print('Введите натуральную степень k:')
k = int(input()) 
 
def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(-100, 101))    
    return list
    
def create_str(sp):
    list = sp[::-1]
    sim = ''
    if len(list) < 0:
        sim = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                sim += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] > 0:
                    sim += ' + '
                    if list [i + 1] < 0:
                        sim += ' '
            elif i == len(list) - 2 and list[i] != 0:
                sim += f'{list[i]}x'
                if list[i + 1] > 0:
                    sim += ' + '
                    if list[i + 1] < 0:
                       sim += ' '
            elif i == len(list) - 1 and list[i] != 0:
                sim += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                sim += ' = 0'
    return sim

koef = create_list(k)
print(create_str(koef))