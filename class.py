class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o 
        
    def do_work(self):  # Properly indented under class
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")  # Fixed typo: "flim" → "film"
            
    def speak(self):  # Properly indented under class
        print(self.name, "i do speak")
        
    def eat(self):  # Properly indented under class
        print(self.name, "i eat rice")

tom = Human("Tom cruise", "actor")
tom.do_work()
tom.speak()
tom.eat()

maria = Human("Maria sharapova", "tennis player")
maria.do_work()
maria.speak()
maria.eat()