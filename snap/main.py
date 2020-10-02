import random
import time

suits = {"Hearts": "\u2665" , "Diamonds": "\u2666", "Spades":"\u2660", 'Clubs':"\u2663"}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': "2", 'Three': "3", 'Four': "4", 'Five': "5", 'Six': "6", 'Seven': "7", 'Eight': "8", 'Nine': "9", 'Ten': "10",
          'Jack': "J",
          'Queen': "Q", 'King': "K", 'Ace': "A"}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits.keys():
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def remove_card(self):
        popped_card = self.deck.pop()
        return popped_card


class Player:

    def __init__(self):
        self.points = 0
        self.collected_cards = []

    def collect_card(self,card):
        if card.rank == "Ace" or card.rank == "Jack":
            self.points += 1
        if (card.rank == "Two" and card.suit == "Clubs") or (card.rank == "Ten" and card.suit == "Diamonds"):
            self.points += 3
        self.collected_cards.append(card)


class Hand:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self,card):
        popped_card = self.hand.pop(self.hand.index(card))
        return popped_card

class Ground:

    def __init__(self):
        self.cards = []
        self._top_card = object

    @property
    def top_card(self):
        if self.cards:
            self._top_card = self.cards[len(self.cards)-1]
        else :
            self._top_card = None
        return self._top_card

    def to_ground(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

while True:     # Game loop

    deck = Deck()
    deck.shuffle()
    player = Player()
    emmi = Player()
    p_hand = Hand()
    e_hand = Hand()
    ground = Ground()

    def enter_to_cont():
        print("\n" * 10)
        print("Enter to continue.".center(180))
        print("\n" * 10)
        input()


    def player_turn():

        play = 1

        while play:

            print("\n"*40)
            print("It's your turn.".center(180))
            print("\n"*15)
            enter_to_cont()
            if ground.top_card:
                print(f"Top card on ground:  {values[ground.top_card.rank]} of {suits[ground.top_card.suit]}".center(180))
            else:
                print("Top card on the ground:  None".center(180))
            print("\n"*2)
            print(f"There are {len(ground.cards)} cards on the ground.".center(180))
            print("\n"*10)
            print("\t"*2, f"Your Score : {player.points}","\t"*13, f"Emmi's Score : {emmi.points}")
            print("\n"*2)
            print("Your Hand:".center(180))
            print("\n"*3)
            for card in p_hand.hand:
                print(f"{p_hand.hand.index(card)+1}. {values[card.rank]} of {suits[card.suit]}".center(180))
                print("\n")
            print("\n"*5)
            print("Choose the card you want to play by its corresponding number.")
            print("\n"*3)
            choice = input()

            try:
                match = 0
                choice = p_hand.hand[int(choice) - 1]
                if ground.top_card:
                    if choice.rank == ground.top_card.rank or choice.rank == "Jack":
                        match = 1
                    ground.to_ground(p_hand.remove_card(choice))
                    if match == 1:
                        if len(ground.cards) == 2:
                            player.points += 10
                            print("\n" * 40)
                            print("Snap!".center(180))
                            enter_to_cont()

                        for card in ground.cards:
                            player.collect_card(card)
                        print("\n"*40)
                        print("You cleared all the cards on the ground!".center(180))
                        enter_to_cont()

                        ground.clear()
                else:
                    ground.to_ground(p_hand.remove_card(choice))
                play = 0

            except:
                print("\n"*40)
                print("Please enter a proper command.".center(180))
                enter_to_cont()


    def emmi_turn():

        print("\n" * 40)
        print("It's Emmi's turn.".center(180))
        print("\n" * 15)
        if ground.top_card:
            print(f"Top card on ground:  {values[ground.top_card.rank]} of {suits[ground.top_card.suit]}".center(180))
        else:
            print("Top card on the ground:  None".center(180))
        print("\n" * 10)
        print("Emmi's thinking.")
        print("\n"*5)
        for i in range(10):
            print(".".center(180))
            time.sleep(0.3)

        emmi_ranks = [card.rank for card in e_hand.hand]

        if ground.top_card:
            if ground.top_card.rank in emmi_ranks:
                emmi_playables = [card for card in e_hand.hand if card.rank == ground.top_card.rank]
                print("\n"*40)
                print(f"Emmi played:  {values[emmi_playables[0].rank]} of {suits[emmi_playables[0].suit]}".center(180))
                enter_to_cont()
                ground.to_ground(e_hand.remove_card(emmi_playables[0]))
                if len(ground.cards) == 2:
                    emmi.points += 10
                    print("\n" * 40)
                    print("Snap!".center(180))
                    enter_to_cont()
                for card in ground.cards:
                    emmi.collect_card(card)
                print("\n" * 40)
                print("Emmi cleared all the cards on the ground!".center(180))
                enter_to_cont()
                ground.clear()
            elif "Jack" not in emmi_ranks:
                print("\n" * 40)
                print(f"Emmi played:  {values[e_hand.hand[0].rank]} of {suits[e_hand.hand[0].suit]}".center(180))
                enter_to_cont()
                ground.to_ground(e_hand.remove_card(e_hand.hand[0]))
            else:
                if len(e_hand.hand) == 1:
                    print("\n" * 40)
                    print(f"Emmi played:  {values[e_hand.hand[0].rank]} of {suits[e_hand.hand[0].suit]}".center(180))
                    enter_to_cont()
                    for card in ground.cards:
                        emmi.collect_card(card)
                    print("\n" * 40)
                    print("Emmi cleared all the cards on the ground!".center(180))
                    enter_to_cont()
                    ground.to_ground(e_hand.remove_card(e_hand.hand[0]))
                    ground.clear()
                elif len(e_hand.hand) > 1:
                    for card in e_hand.hand:
                        if card.rank != "Jack":
                            print("\n" * 40)
                            print(f"Emmi played:  {values[card.rank]} of {suits[card.suit]}".center(180))
                            ground.to_ground(e_hand.remove_card(card))
                            enter_to_cont()
                            break
        elif "Jack" not in emmi_ranks:
            print("\n"*40)
            print(f"Emmi played:  {values[e_hand.hand[0].rank]} of {suits[e_hand.hand[0].suit]}".center(180))
            enter_to_cont()
            ground.to_ground(e_hand.remove_card(e_hand.hand[0]))
        else:
            if len(e_hand.hand) == 1:
                print("\n" * 40)
                print(f"Emmi played:  {values[e_hand.hand[0].rank]} of {suits[e_hand.hand[0].suit]}".center(180))
                enter_to_cont()
                ground.to_ground(e_hand.remove_card(e_hand.hand[0]))
            elif len(e_hand.hand) > 1:
                for card in e_hand.hand:
                    if card.rank != "Jack":
                        print("\n" * 40)
                        print(f"Emmi played:  {values[card.rank]} of {suits[card.suit]}".center(180))
                        ground.to_ground(e_hand.remove_card(card))
                        enter_to_cont()
                        break


    print("\n"*40)
    print("Hello and welcome to Snap!".center(180))
    enter_to_cont()

    for i in range(4):
        ground.to_ground(deck.remove_card())

    turn = 1

    while True:     # Turn loop

        for i in range(4):
            p_hand.add_card(deck.remove_card())
            e_hand.add_card(deck.remove_card())

        print("\n"*40)
        print(f"TURN: {turn}".center(180))
        print("\n"*5)
        print("Cards are being dealt. Please wait...".center(180))
        print("\n"*10)
        time.sleep(2)
        for i in range(10):
            print(".".center(180))
            time.sleep(0.3)


        while p_hand.hand or e_hand.hand:     # Play loop

            player_turn()
            emmi_turn()
        turn += 1
        if not deck.deck:


            print("\n"*40)
            print("No cards in deck. Game over.".center(180))
            print("\n"*5)
            if len(player.collected_cards) > len(emmi.collected_cards):
                player.points += 3
            elif len(player.collected_cards) < len(emmi.collected_cards):
                emmi.points += 3
            else:
                pass
            print(f"Player points: {player.points} | Emmi points: {emmi.points}".center(180))
            print("\n"*3)
            print(f"Player collected {len(player.collected_cards)} cards, Emmi collected {len(emmi.collected_cards)}.")
            print("\n"*5)
            if player.points < emmi.points:
                print("Emmi wins.".center(180))
            elif player.points == emmi.points:
                print("It's a tie.".center(180))
            else:
                print("Player wins!".center(180))
            print("\n"*5)
            print("Press 'r' if you want to try again, or any button if you want to quit the game.".center(180))
            retry = input()
            if retry.lower() == "r":
                break
            else:
                __import__('sys').exit()