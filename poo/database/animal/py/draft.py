class Animal:
    def __init__(self,species :str, sound :str):
        self.species  = species
        self.age : int = 0
        self.sound = sound
    
    def makeSound (self) -> str:
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        else:
            return self.sound
    
    def ageBy(self,increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")
            

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
def main():
    animal = Animal ("","")

    while True:
        line : str = input()
        print("$" + line)
        args : list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show" :
            print(animal)
        elif args[0] == "grow":
            increment = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            print(animal.makeSound())
main()

    




        
