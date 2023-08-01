import random
from python import clear


def black_jack():
    game_over = False
    bust = False
    def deal(deck):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        rand_card = random.choice(cards)
        deck.append(rand_card)
    def calc(users_deck, dealer):
        if sum(users_deck) == sum(dealer):
            print("it's a draw")
        elif sum(users_deck) == 21 and len(users_deck) == 2:
            print("You have a black jack, YOU WIN!!")
        elif sum(dealer) > 21:
            print(f"Dealers total = {sum(dealer)}, opponent went over,\nYOU WIN!!")
        elif sum(users_deck) > sum(dealer):
            print(f"Your total is {sum(users_deck)} while the opponents total is {sum(dealer)},\nYOU WIN!!")
        else:
            print(f"Your total was {sum(users_deck)} while dealers total was {sum(dealer)}\n YOU LOSE")
    users_deck = []
    dealer = []
    deal(deck = users_deck)
    deal(deck = users_deck)
    print(users_deck)
    deal(deck = dealer)
    print(dealer)
    deal(deck = dealer)
    print(f"Your current total is {sum(users_deck)}.")
    while game_over == False and bust == False:
        if sum(users_deck) > 21:
            bust = True
            print(f"Your total is {sum(users_deck)}, you went over, sorry its a bust,\nYOU LOSE")
            break
        Hit_again = input("would you like to hit again? \nY/N ")
        hit_again = Hit_again.lower()
        if hit_again == "y":
            deal(deck = users_deck)
            if 11 in users_deck and sum(users_deck) > 20:
                users_deck.remove(11)
                users_deck.append(1)
            elif 11 in dealer and sum(dealer) > 20:
                dealer.remove(11)
                dealer.append(1)
            print(f"{users_deck} your current total is {sum(users_deck)}")
        elif hit_again == "n":
            if sum(dealer) < 17:
                deal(deck = dealer)
                calc(users_deck = users_deck, dealer = dealer)
                game_over = True
            else:
                calc(users_deck = users_deck, dealer = dealer)
                game_over = True
        else:
            print("invalid input, try again.")
    Replay = input("Do you want to play again? \nY/N ")
    replay = Replay.lower()
    if replay == "y":
        clear()
        black_jack()
    else:
        print("Good game.")   
question = input("Do you want to play black jack? \nY/N ")
Question = question.lower()
if Question == "y":
    black_jack()
elif Question == "n":
    print("Then what are you doing here?")
else:
    print("invalid input")