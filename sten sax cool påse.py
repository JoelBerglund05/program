import random

player1 = random.randint(1,3)
player2 = random.randint(1,3)

play = input("vill du börja spela?").lower()
play2 = 0
while play2 == 0:
    while play == "j":
        if player1 == 1 and player2 == 2:
            print("spelare 1: sten spelare 2: sax")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        elif player2 == 1 and player1 == 2:
            print("spelare 2: sten spelare 1: sax")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        elif player1 == 1 and player2 == 3:
            print("spelare 1: sten spelare 2: påse")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        elif player2 == 1 and player1 == 3:
            print("spelare 2: sten spelare 1: påse")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        elif player1 == 2 and player2 == 3:
            print("spelare 2: sax spelare 1: påse")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        elif player2 == 2 and player1 == 3:
            print("spenare 1: sax spelare 2: påse")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        elif player1 + player2 == player1 * 2:
            print("lika")
            player1 = random.randint(1,3)
            player2 = random.randint(1,3)
            play = input("vill du börja spela?").lower()
        else:
            print(player1, player2)
            play2 += 1
            break

    if play == "n":
      print("välkomen åter")
      break
    elif play != "n" or play != "j":
        print("något blev fel")
        play = input("vill du börja spela?").lower()
