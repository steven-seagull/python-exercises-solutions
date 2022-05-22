class Exercise:
    @staticmethod
    def getString() -> str:
        return input("Input?\n")
    
    @staticmethod
    def printString(string) -> None:
        print(string.upper())

string = Exercise.getString()
Exercise.printString(string)

