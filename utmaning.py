from random import randint

class Tarningsspel:
    def __init__(self, spelare1, spelare2):
        self.spelare1 = spelare1
        self.spelare2 = spelare2
        self.poang_spelare1 = 0
        self.poang_spelare2 = 0

    def kasta(self):
        return randint(1, 6)

    def spela_runda(self):
        result_spelare1 = self.kasta()
        result_spelare2 = self.kasta()

        print(f"\n{self.spelare1} kastade: {result_spelare1}")
        print(f"\n{self.spelare2} kastade: {result_spelare2}")

        if result_spelare1 == result_spelare2:
            print("Kastade samma värde. Ingen får en poäng")
        elif result_spelare1 > result_spelare2:
            self.poang_spelare1 += 1
            print(f"{self.spelare1} har kastat högre och vinner!!")
        else:
            self.poang_spelare2 += 1
            print(f"{self.spelare2} har kastat högre och vinner!!")

        print(f"\n{self.spelare1} har: {self.poang_spelare1} poäng")
        print(f"{self.spelare2} har: {self.poang_spelare2} poäng\n")
        print("_____________________________________________________")



spel = Tarningsspel(input("Ange spelare 1 namn: "), input("Ange spelare 2 namn: "))
max_poang = int(input("Hur många poäng tills nån har vunnit: "))


while max(spel.poang_spelare1, spel.poang_spelare2) < max_poang:

    spel.spela_runda()

if spel.poang_spelare1 == max(spel.poang_spelare1, spel.poang_spelare2):
    print(f"{spel.spelare1} vann!!!")

else:
    print(f"{spel.spelare2} vann!!!")