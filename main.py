MAX_ATTEMPTS = 3

def get_number(prompt, operator=None):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            number = float(input(prompt))
            if operator == "/" and number == 0:
                print("Ділення на 0 неможливе! Спробуйте ще раз.")
                attempts += 1
                continue
            return number
        except ValueError:
            print("Ви ввели не число!")
            attempts += 1
    return None

def get_operator():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_operator = input("Виберіть операцію (+, -, *, /): ")
        if len(user_operator) == 1 and user_operator in "+-*/":
            return user_operator
        else:
            print("Невідома операція!")
            attempts += 1
    return None

def calculate(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
    return None

def calculator():
    a = get_number("Введіть перше число: ")
    operator = get_operator()
    b = get_number("Введіть друге число: ", operator)

    if any(i is None for i in (a, b, operator)):
        print("Щось пішло не так :( Спробуйте ще раз")
        return


    result = calculate(a, b, operator)
    if result is not None:
        print("Результат:", result)
    else:
        print("От халепа! Десь щось не то, не можу порахувать")

    try_again = input("Спробуєм ще раз? (так/ні) ").lower().strip()
    if try_again == "так":
        calculator()
    elif try_again == "ні":
        print("Тоді бувай!")
    else:
        print("Невідомий варіант відповіді. Завершуємо.")

calculator()