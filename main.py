from random import randint

class Spelare():
    def __init__(self, player, points=0):
        self.player_name = player
        self.points = points

    def kasta(self):
        result = randint(1, 6)
        return result

    def vinn_runda(self):
        self.points += 1


player1 = Spelare(input("Ange namn för spelare 1: "))
player2 = Spelare(input("Ange namn för spelare 2:"))

while max(player1.points, player2.points) < 5:

    result_player1 = player1.kasta()
    result_player2 = player2.kasta()

    print(f"\n{player1.player_name} kastade: {result_player1}")
    print(f"{player2.player_name} kastade: {result_player2}")


    if result_player1 == result_player2:
        print("Kastade samma värde. Ingen får en poäng")
    elif result_player1 > result_player2:
        player1.vinn_runda()
        print(f"{player1.player_name} har kastat högre och vinner!!")
    else:
        player2.vinn_runda()
        print(f"{player2.player_name} har kastat högre och vinner!!")

    print(f"\n{player1.player_name} har: {player1.points} poäng")
    print(f"{player2.player_name} har: {player2.points} poäng\n")
    print("_____________________________________________________")



if player1.points == max(player1.points, player2.points):
    print(f"{player1.player_name} vann!!!")

else:
    print(f"{player2.player_name} vann!!!")

    











