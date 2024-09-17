# write path to your file here
path = "content.txt"

with open("content.txt", "r", encoding="utf8") as f:
    tasks = f.readlines()
    
import random
randomised = False
    
try:
    while True:
        try:
            type = int(input("Как мне тебя спрашивать?\nСпрашиваю то, что ты написано слева, отвечаешь то, что ты написано справа - 1\nСпрашиваю то, что написано справа, отвечаешь то, что написано слева - 2\nВыйти - 0\n\nВведи подходящую цифру: "))

            if type == 0:
                break
            elif type not in [1, 2]:
                print("Получен неизвестный вариант ответа")
            else:
                while True:
                    try:
                        order = int(input("В каком порядке задаю вопросы?\nВ таком, как написано - 1\nВразброс - 2\nНазад - 0\n\nВведи подходящую цифру: "))
                        
                        if order == 0:
                            break
                        elif order not in [1, 2]:
                            print("Получен неизвестный вариант ответа")
                        else:
                            if order == 2:
                                randomised = True
                            while True:
                                try:
                                    exit = int(input("После того, как вижу правильный ответ, я:\nСпрашиваю, пока не получу правильный ответ - 1\nНачинаю опрос заново - 2\nПропускаю вопрос - 3\nНазад - 0\n\nВведи подходящую цифру: "))
                                    
                                    if exit == 0:
                                        break
                                    elif exit not in [1, 2, 3]:
                                        print("Получен неизвестный вариант ответа")
                                    else:
                                        print("Начинаю опрос.")
                                        if randomised: random.shuffle(tasks)
                                        
                                        for i in range(len(tasks)):
                                            task = tasks[i]
                                            splitted = task.split(";")
                                            if type == 1:
                                                question = splitted[0]
                                                answer = splitted[1]
                                            else:
                                                question = splitted[1]
                                                answer = splitted[0]
                                                
                                            if answer.lower() == input(f"Вопрос {i+1} из {len(tasks)}.\n{question}\n"):
                                                print("Правильный ответ! Продолжаем\n")
                                            else:
                                                if exit == 1:
                                                    text = f"Неверный ответ! Попробуй еще раз.\nВопрос {i+1} из {len(tasks) + 1}.\n{question}\n"
                                                    while input(text) != answer:
                                                        ...
                                                    else:
                                                        print("Правильный ответ! Продолжаем\n")
                                                elif exit == 2:
                                                    print("Неправильный ответ! Начинаем заново...\n")
                                                    break
                                                elif exit == 3:
                                                    print(f"Неправильный ответ! Правильный ответ - \"{answer}\" Продолжаем...\n")
                                except ValueError:
                                    print("Не удалось получить число из того, что ты ввел(-а). Давай еще раз.\n")
                    except ValueError:
                        print("Не удалось получить число из того, что ты ввел(-а). Давай еще раз.\n")
        except ValueError:
            print("Не удалось получить число из того, что ты ввел(-а). Давай еще раз.\n")
except KeyboardInterrupt:
    quit()