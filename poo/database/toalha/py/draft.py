class Towel:
    def __init__(self, color: str, size: str):
            self.color: str = color
            self.size: str = size
            self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("Toalha enxarcada")
            self.wetness = self.getMaxWetness() 

    def getMaxWetness(self) -> int:
        if self.size == "p":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
   
    def wringOut(self) -> None:
         self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0

    def show(self) -> None:
         print(self)
    
    def __str__(self) -> str:
         return f"{self.color}{self.size}{self.wetness}"
    
         
    #testando
doguito = Towel("azul", "M")
print(doguito)
doguito.dry(15)
print(doguito)
doguito.dry(10)
print(doguito)

vitoria = Towel("rosa", "P")
print(vitoria)
vitoria.dry(5)
print(vitoria)
vitoria.dry(10)
print(vitoria)

    