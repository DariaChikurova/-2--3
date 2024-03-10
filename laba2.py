def zadanie1():
    a=input("введите пароль: ")
    b=input("введите пароль еще раз: ")
    if len(a)<6 and len(b)<6:
        print("проверьте длину")
    elif a==b:
        print("совпадает")
    else:
        print("не совпадает")


def zadanie2():
    a = int(input("введите номер места: "))
    if a in range(1, 56):
        print("место найдено")
    else:
        print("место не найдено")
    if a % 2 ==0:
        print("место внизу")
    else:
        print("место снизу")
    if a ==5 or a==6 or a==11 or a==12 or a==17 or a==18 or a==23 or a==24 or a==29 or a==30 or a==35 or a==36 or a==41 or a==42 or a==47 or a==48 or a==53 or a==54:
        print("места сбоку")
    else:
        print("места не сбоку")

def zadanie3():
    year = int(input("Введите год: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Год високосный")
    else:
        print("Это год не високосный")

def zadanie4():
    color1 = input("введите цвет: ")
    color2 = input("введите цвет: ")
    if ((color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный")):
        print("фиолетовый")
    elif ((color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный")):
        print("оранжевый")
    elif ((color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий")):
        print("зеленый")
    else:
        print("введите правильно цвета: ")

while True:
    choice = input("\n1-1 \n2-2 \n3-3 \n4-4")
    match choice:
        case "1":
            zadanie1()
        case "2":
            zadanie2()
        case "3":
            zadanie3()
        case "4":
            zadanie4()
    if choice == "0":
        break
