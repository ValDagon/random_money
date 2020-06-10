from random import randint
 
i = 1
j = 1
tail_counter = 0
eagle_counter = 0

eagle_zero = 0
eagle_one = 0
eagle_two = 0
eagle_three = 0
eagle_four = 0
eagle_five = 0
eagle_six = 0
eagle_seven = 0
eagle_eight = 0
eagle_nine = 0
eagle_ten = 0

print("Номер опыта", "Решка", "Орёл")

while i <= 1000:
    j = 1
    while j <= 10: 
        money = randint(0, 1)
        if money == 0:
            tail_counter += 1
        elif money == 1:
            eagle_counter += 1
        else:
            print("Ошибка!", money)

        j += 1
        
    if eagle_counter == 0:
        eagle_zero += 1
    elif eagle_counter == 1:
        eagle_one += 1
    elif eagle_counter == 2:
        eagle_two += 1        
    elif eagle_counter == 3:
        eagle_three += 1
    elif eagle_counter == 4:
        eagle_four += 1
    elif eagle_counter == 5:
        eagle_five += 1
    elif eagle_counter == 6:
        eagle_six += 1
    elif eagle_counter == 7:
        eagle_seven += 1        
    elif eagle_counter == 8:
        eagle_eight += 1
    elif eagle_counter == 9:
        eagle_nine += 1
    elif eagle_counter == 10:
        eagle_ten += 1
    else:
        print("Что-то пошло не так", eagle_counter)


    print("\n    ", i, "     ", tail_counter, "   ", eagle_counter)

    tail_counter = 0
    eagle_counter = 0
    i += 1

print("\n", eagle_zero, eagle_one, eagle_two, eagle_three, eagle_four, eagle_five, eagle_six, eagle_seven, eagle_eight, eagle_nine, eagle_ten)
print("Сумма: ", eagle_zero + eagle_one + eagle_two + eagle_three + eagle_four + eagle_five + eagle_six + eagle_seven + eagle_eight + eagle_nine + eagle_ten)