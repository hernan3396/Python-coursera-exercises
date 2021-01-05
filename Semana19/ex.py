class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, iname):
        self.name = iname
        print("i am become", self.name)

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("im out", self.name)


an = PartyAnimal("gyal")
an.x
pa = PartyAnimal("pepe")

an.party()
