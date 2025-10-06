class Carro: 
    def __init__(self):
        self.passengers = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
        self.km = 0
    def __str__(self) -> str:
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"
    def enter (self) -> None:
         if self.passengers < self.passMax:
              self.passengers +=1
         else:
              print("fail: limite de pessoas atingido")
    def leave(self):
         if self.passengers > 0:
             self.passengers -= 1
         else:
              print("fail: nao ha ninguem no carro")
    def fuel(self, amount :int) -> None:
         if self.gas + amount > self.gasMax:
              self.gas = self.gasMax
         else:
              self.gas += amount
    def drive(self, distance: int) -> None:
         if self. passengers == 0:
            print("fail: nao ha ninguem no carro")
            return
         if self.gas == 0:
              print("fail: tanque vazio")
              return
         if distance <= self.gas:
              self.km += distance
              self.gas -= distance
         else:
              print(f"fail: tanque vazio apos andar {self.gas} km")
              self.km += self.gas
              self.gas = 0


def main ():
        carro = Carro()
        while True:
            line : str = input()
            print("$" + line)
            args = line.split()
            if args[0] == "end":
               break
            elif args[0] == "show":
                print(carro)
            elif args[0] == "enter":
                 carro.enter()
            elif args [0] == "leave":
                 carro.leave()
            elif args [0] == "fuel":
                amount = int(args[1])
                carro.fuel(amount)
            elif args[0] == "drive":
                 distance = int(args[1])
                 carro.drive(distance) 
main ()