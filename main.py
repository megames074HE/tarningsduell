from random import randint


class Spelare():
    def __init__(self, player, points=None):
        self.player = player
        self.points = points

    def kasta(self):
        result = randint(1, 6)
        return result


player1 = Spelare("ola")
player2 = Spelare("conny")

result = player1.kasta()

print(result)





