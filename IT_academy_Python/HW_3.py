#ввод данных
input_data = False
while input_data==False: 
    try:
        a = int(input("Введите целое число 1: "))
        b = int(input("Введите целое число 2: "))
        c = int(input("Введите целое число 3: "))
        input_data=True
    except ValueError:
         print ("Только целые числа")
         input_data=False

lst = (a, b, c)

#Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)
(0 not in lst) and print("нет нулевых значений")

#Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень
(0 in lst) and print(lst.index(0))
(len([x for x in lst if x==0])==3) and print("Введены все нули")

#Если первое значение больше чем сумма второго и третьего вывести a - b - c
(a>(b+c)) and print(a-b-c)
    
#Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
(a>50 and (b>a or c>a)) and print("Вася")

#Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
((a>5) or (b==7 and c==7)) and print("Петя")
