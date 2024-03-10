import random
def zadanie1():
    n = int(input("Введите количество слов: "))
    result = ""
    for i in range(n):
        result+=input("введите слово: ")
        result+=" "
    print(result)

def zadanie2():
    result = ""
    while True:
        choice = input("stop? ")
        if choice == "stop":
            break
        else:
            result += choice
        result += " "
    print(result)

def zadanie3():
    word = input("Введите слово: ")
    if "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

def zadanie4():
    right = 0
    wrong = 0
    while wrong < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 + num2
        user_answer = int(input(f"{num1} + {num2} = "))
        if user_answer == num1 + num2:
            print("Правильно!")
            right += 1
        else:
            print("Ответ неверный")
            wrong += 1
    print(f"Игра окончена. Правильных ответов: {right}")

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
