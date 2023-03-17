class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Mooooo"

milky = Cow("Milky White")
milky.speak()
