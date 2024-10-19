print("Задача:Выписывать из этого списка только положительные числа до тех пор,"
      " пока не встретите отрицательное или не закончится список"
      )
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
confirmation = input("Вы готовы начать?Напишите 'Да' или 'Нет' : ")
if confirmation == 'Да' or confirmation == 'да' or confirmation == 'ДА' :
    print (my_list)
    print("Ответ: ")
    first = 0
    while first < len (my_list) :
        if my_list[first] >= 0 :
            if my_list[first] != 0 :
                print (my_list[first])
                first = first + 1
            elif my_list[first] == 0 :
                first = first + 1
                continue
        else:
             break
else:
    print ("До свидания!")