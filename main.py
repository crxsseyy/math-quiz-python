import random

def start_quiz():
    print("--- МОЙ ПЕРВЫЙ IT-ПРОЕКТ: MATH QUIZ ---")
    name = input("Введи свое имя, герой: ")
    score = 0
    goal = 5 # Нужно набрать 5 баллов
    
    print(f"\nПривет, {name}! Твоя цель — набрать {goal} баллов.")
    print("За правильный ответ +1, за ошибку -1. Погнали!\n")

    while score < goal:
        # 1. Выбираем случайные числа
        a = random.randint(1, 15)
        b = random.randint(1, 10)
        
        # 2. Выбираем операцию: + или *
        operation = random.choice(['+', '*'])
        
        if operation == '+':
            correct_answer = a + b
        else:
            correct_answer = a * b

        # 3. Задаем вопрос
        print(f"Сколько будет {a} {operation} {b}?")
        
        # Защита от ошибок ввода (Try/Except)
        try:
            user_answer = int(input("Твой ответ: "))
        except ValueError:
            print("Эй, вводи только цифры! Штрафной балл за невнимательность.")
            score -= 1
            continue

        # 4. Проверка результата
        if user_answer == correct_answer:
            score += 1
            print(f"✅ Красава! Твой счет: {score}")
        else:
            score -= 1
            print(f"❌ Мимо! Правильно было {correct_answer}. Твой счет: {score}")

    print(f"\nПОЗДРАВЛЯЮ, {name.upper()}!")
    print("Ты прошла викторину и готова покорять GitHub!")

# Запуск игры
start_quiz()

