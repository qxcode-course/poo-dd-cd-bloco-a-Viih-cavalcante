
class Calculadora:
    def __init__(self, batteryMax: int):
        self.display = 0
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment: int):
        if self.battery + increment <= self.batteryMax:
            self.battery += increment
        else:
            self.battery = self.batteryMax

    def sum(self, a: int, b: int):
        if self.battery > 0:
         self.display = a + b
         self.battery -= 1
        else:
            print("fail: bateria insuficiente")    

    def div(self, den: int, num: int):
        if self.battery > 0:
            if num == 0:
             print("fail: divisao por zero")
             self.battery -=1
            elif num != 0:
                self.display = den / num
                self.battery -=1
        else:
                print("fail: bateria insuficiente")

def main():
    calc = Calculadora(0)
    while True:
        line: str = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            calc = Calculadora(int(args[1]))
        elif args[0] == "show":
            print(calc)
        elif args[0] == "charge":
            increment = int(args[1])
            calc.charge(increment)
        elif args[0] == "sum":
           calc.sum(int(args[1]), int(args[2]))
        elif args[0] == "div":
          calc.div(int(args[1]), int(args[2]))
        else:
            print("fail: comando desconhecido")
main()