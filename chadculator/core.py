import time

class Chadculator:
    MAX_ATTEMPTS = 3

    def __init__(self, insult_manager):
        self.insulter = insult_manager

    def get_number(self, prompt, operator=None):
        attempts = 0
        while attempts < self.MAX_ATTEMPTS:
            user_input = input(prompt).strip().lower()

            if user_input in ["перше число", "друге число", "число"]:
                attempts += 1
                if attempts < self.MAX_ATTEMPTS:
                    self.insulter.insult("troll")
                continue
            try:
                number = float(user_input)
                if operator == "/" and number == 0:
                    attempts += 1
                    if attempts < self.MAX_ATTEMPTS:
                        self.insulter.insult("zero_division")
                    continue
                return number
            except ValueError:
                attempts +=1
                if attempts < self.MAX_ATTEMPTS:
                    self.insulter.insult("wrong_input_number")

        self.insulter.insult("burnout")
        time.sleep(5)
        return None

    def get_operator(self):
        attempts = 0
        while attempts < self.MAX_ATTEMPTS:
            user_operator = input("Вибери операцію (+, -, *, /): ")
            if len(user_operator) == 1 and user_operator in "+-*/":
                return user_operator
            else:
                attempts += 1
                if attempts < self.MAX_ATTEMPTS:
                    self.insulter.insult("unknown_operator")

        self.insulter.insult("burnout")
        time.sleep(5)
        return None

    def calculate(self, a, b, operator):
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

    def run(self):
        while True:
            a = self.get_number("Введи перше число: ")
            if a is None:
                continue

            operator = self.get_operator()
            if operator is None:
                continue

            b = self.get_number("Введи друге число: ", operator)
            if b is None:
                continue

            # if any(i is None for i in (a, b, operator)):
            #     continue

            result : int = self.calculate(a, b, operator)
            if result is not None and abs(result) < 10000000:
                print("Результат:", result)
            elif abs(result) >= 10000000:
                print("🗣️ Це десь до**я виходить")
            else:
                self.insulter.insult("general_fail")

            try_again = input("Спробуєш ще раз? (так/ні) ").lower().strip()
            if try_again == "так":
                continue
            elif try_again == "ні":
                print("Нарешті я вільний")
                break
            else:
                self.insulter.insult("general_fail")
                break