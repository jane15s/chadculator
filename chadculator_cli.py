from chadculator.core import Chadculator
from chadculator.insults import InsultManager

def main():
    insulter = InsultManager()
    chad = Chadculator(insulter)
    chad.run()

if __name__ == "__main__":
    main()