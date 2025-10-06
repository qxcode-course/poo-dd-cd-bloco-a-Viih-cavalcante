class Towel:
    def __init__(self, color :str, size :str):
        self.color = color
        self.size = size
        self.Wetness = 0
    
    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size =="G":
            return 30
        return 0
    
    def dry(self, amount :int) -> None:
        self.Wetness += amount
        if self.Wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.Wetness = self.getMaxWetness()
        
    def wringOut(self) -> None:
        self.Wetness = 0

    def isDry(self) -> bool:
       return self.Wetness == 0
    
    def mostrar(self) -> None :
        print(self)

    def __str__(self) -> str:
        return f"Cor: {self.color }, Tamanho: {self.size }, Umidade: {self.Wetness}"

def main():
    toalha = Towel("","")
    while True:
        line : str = input()
        print("$" + line)
        args : list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "mostrar":
            print(toalha)
        elif args[0] == "torcer":
            toalha.wringOut()
        elif args[0] == "seca":
            print("sim" if toalha.isDry() else "nao")
        elif args[0] == "enxugar":
            amount: int = int(args[1])
            toalha.dry(amount)
    
main()


        