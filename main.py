user_choise = ""
chet1 = 10000
chet2 = 200

while user_choise != "7":


    print("Добро пожаловать  банкомат".upper())

    print("МЕНЮ\nВыберите действие:\n1. Баланс всего\n2. Баланс на первом счете\n3. Баланс на втором "
                     "счете\n4. Вывод средств\n5. Внесение средств\n6. Перенос средств между счетами\n7. Выход")
    
    print(40*'-')

    user_choise = input("Введите выбранный номер пункта - ")
    if user_choise == "1":
        print("Всего средств на счетах - ", chet1 + chet2 '$')
    elif user_choise == "2":
        print(f"Баланс на первом счете - {chet1}$")
    elif user_choise == "3":
        print(f"Баланс на втором счете - {chet2}$")
    elif user_choise == "4":
        user_choise = input("С какого счета выводим средства, с первого или второго?")
        if user_choise == "1":
            user_choise = int(input("Сколько средств снимаем?"))
            if user_choise <= chet1:
                print("Вы сняли", chet1 - user_choise, "$, на балансе счета осталось - ", chet1- user_choise,"$")
        elif user_choise == "2":
            user_choise = int(input("Сколько средств снимаем?"))
            if user_choise <= chet2:
                print("Вы сняли", chet2 - user_choise, "$, на балансе счета осталось - ", chet2 - user_choise,"$")
    elif user_choise == "5":
        user_choise = input("На какой счет вносим деньги?")
        if user_choise == "1":
            user_choise = int(input("Сколько средств вводим? - "))
            print("Вы ввели на первый счет - ", user_choise, "$, Баланс первого счета - ", user_choise + chet1)
        elif user_choise == "2":
            user_choise = int(input("Сколько средств вводим? - "))
            print("Вы ввели на второй счет - ", user_choise, "$, Баланс второго счета - ", user_choise + chet2)
    elif user_choise == "7":
        print("Выход из программы")
        print(40 * '-')
        exit()