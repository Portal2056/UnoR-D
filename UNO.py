from random import *
import time
# Creates numbers and basic identities of specal cards
class color:
   def __init__(self, color, deck2=0):
       self.zero = color + '0'
       self.one = color + '1'
       self.two = color + '2'
       self.three = color + '3'
       self.four = color + '4'
       self.five = color + '5'
       self.six = color + '6'
       self.seven = color + '7'
       self.eight = color + '8'
       self.nine = color + '9'
       self.dT = color + 'dT'
       self.skip = color + 'skip'
       self.reverse = color + 'rev'
       if deck2 == 1:
           self.list = [self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,
                       self.dT,self.skip,self.reverse]
       else:
           self.list = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,
                        self.nine, self.dT,self.skip,self.reverse]

# Creates wild cards for creation of decks and in-game play
class wild:
   def __init__(self):
       self.dF = 'dF'
       self.cc = 'cc'
       self.list = [self.dF, self.cc] * 4

# Defines colors and wild card sets
r = color(color='R_')
y = color(color='Y_')
g = color(color='G_')
b = color(color='B_')
r2 = color(color='R_',deck2=1)
y2 = color(color='Y_',deck2=1)
g2 = color(color='G_',deck2=1)
b2 = color(color='B_',deck2=1)
wild = wild()

# Defines individual player hands
player1_deck, bot1_deck, bot2_deck, bot3_deck, sortedDeck = [], [], [], [], []

# Handles sorting of decks and player order in-game
playerOrder = ["Player 1", "Bot 1", "Bot 2", "Bot 3"]
turn_deck = [player1_deck, bot1_deck, bot2_deck, bot3_deck]

# Creates decks through giving random cards to each player (7 to 4 = 28 cards with additional topCard placed)
class deck:
    def __init__(self):
        self.deck = r.list + y.list + g.list + b.list + r2.list + y2.list + g2.list + b2.list + wild.list

    def make_deck(self):
        for i in range(4):
            if i == 0:
                for j in range(7):
                    card = randint(1,len(deck.deck)-1)
                    player1_deck.append(self.deck[card])
                    self.deck.__delitem__(card)
            elif i == 1:
                for j in range(7):
                    card = randint(1,len(deck.deck)-1)
                    bot1_deck.append(self.deck[card])
                    self.deck.__delitem__(card)
            elif i == 2:
                for j in range(7):
                    card = randint(1,len(deck.deck)-1)
                    bot2_deck.append(self.deck[card])
                    self.deck.__delitem__(card)
            elif i == 3:
                for j in range(7):
                    card = randint(1,len(deck.deck)-1)
                    bot3_deck.append(self.deck[card])
                    self.deck.__delitem__(card)

# Creates function for drawing the first card to play off of
    def drawCard(self):
        global topCard
        card = randint(1, len(deck.deck) - 1)
        topCard = self.deck[card]
        while (topCard.endswith('cc') or topCard.endswith('dF') or topCard.endswith('dT') or topCard.endswith('rev')
            or topCard.endswith('skip')):
            card = randint(1, len(deck.deck) - 1)
            topCard = self.deck[card]
        self.deck.__delitem__(card)

# Function to sort a deck, namely "player1_deck" due to it being the only visible hand
def sortdeck(deck):
    global card_types
    rSort, ySort, gSort, bSort, wSort, num_sorted_deck = [], [], [], [], [], []
    #Sort by number
    for i in range(10):
        for card in deck:
            if card.endswith('_' + str(i)):
                num_sorted_deck.append(card)
    card_types = ['cc', 'dT', 'dF', 'rev', 'skip']
    for i in range(5):
        for card in deck:
            if card.endswith(card_types[i]):
                num_sorted_deck.append(card)

    # Goes through and sorts by color
    for i, card in enumerate(num_sorted_deck):
        if card.startswith('R_'):
            rSort.append(card)
        if card.startswith('Y_'):
            ySort.append(card)
        if card.startswith('G_'):
            gSort.append(card)
        if card.startswith('B_'):
            bSort.append(card)
        if card.startswith('cc') or card.startswith('dF'):
            wSort.append(card)
    global sortedDeck
    sortedDeck = rSort + ySort + gSort + bSort + wSort
    print(sortedDeck)

# Creates a function to place cards
def cardPlace():
    global ph, topCard, cardChoice, player1_deck
    cardChoice = input("What card do you want to play? ")
    while cardChoice not in validCardList:
        cardChoice = input("What card do you want to play? ")
    if cardChoice in validCardList:
        print("You placed " + str(cardChoice) + ".")
        player1_deck.remove(cardChoice)
        topCard = cardChoice


# Checks for valid (playable/legal) cards during a player turn
validCardList = []

def validCardCheck(hand, bot=''):
    global turn, card, topCard, ph, validCardList
    validCardList = []
    for card in hand:
        if card.startswith(topCard[0]) or card.endswith(topCard[-1]) or card.endswith('cc') or card.endswith('dF'):
            validCardList.append(card)
    if playerOrder[turn] == "Player 1":
        if validCardList == [] and player1_deck != []:
            print("You have no playable cards in your hand. You are forced to draw a card from the deck.")
            addCard(player1_deck)
            sortdeck(player1_deck)
            for card in hand:
                if card.startswith(topCard[0]) or card.endswith(topCard[-1]) or card.endswith('cc') or card.endswith('dF'):
                    validCardList.append(card)
            if validCardList != []:
                print("Valid cards in your deck are {}.".format(validCardList))
                cardPlace()
        else:
            print("Valid cards in your deck are {}.".format(validCardList))
    else:
        if validCardList == []:
            print("{} had no playable cards and was forced to draw.".format(bot))
            addCard(hand)
            print(str(playerOrder[(turn + 1) % 4]) + ", it's your turn!")
            turn = (turn + 1) % 4

        else:
            pickRandCard = randint(0,len(validCardList)-1)
            topCard = validCardList[pickRandCard]
            hand.remove(validCardList[pickRandCard])
    ph = topCard

# Adds card to a given deck, removing it from the mainDeck's list in doing so
def addCard(deck1):
    card = randint(0, len(deck.deck) - 1)
    print(card, 'card')
    print(deck.deck[card], 'deck.deck[card]')
    print(deck.deck, 'deck.deck')
    deck.deck.remove(deck.deck[card])
    deck1.append(deck.deck[card])

stackCount = 0

def revDeck(deck):
    global turn
    if topCard.endswith('rev'):
        playerOrder.reverse()
        turn_deck.reverse()
        turn = (turn + 1) % 4

def skipCard():
    global turn
    if topCard.endswith('skip'):
        if turn == 3:
            turn = 0
        else:
            turn += 1

def drawTwo(deck):
    currentDeck = 0
    deckList = [player1_deck, bot1_deck, bot2_deck, bot3_deck]
    turntemp = (turn + 1) % 4
    if deck == player1_deck:
        currentDeck = 0
    elif deck == bot1_deck:
        currentDeck = 1
    elif deck == bot2_deck:
        currentDeck = 2
    elif deck == bot2_deck:
        currentDeck = 3
    for d in range(2):
        addCard(deck)
    print(str(playerOrder[turntemp]) + " has to draw 2 cards.")
    print(len(deckList[currentDeck]) + 1, 'length of ' + str(playerOrder[turntemp]) + '\'s deck')

def drawFour(deck):
    global card, topCard, turn
    turntemp = (turn + 1) % 4
    for d in range(4):
        addCard(turn_deck[turntemp])
    print(str(playerOrder[turntemp]) + " has to draw 4 cards.")
    changeColor(deck)

def changeColor(deck_player):
    global card, colorList, colorChoice, topCard, turn
    if playerOrder[turn] == "Player 1":
        if topCard.endswith('cc') or topCard.endswith('dF'):
            colorList = ['RED', 'YELLOW', 'GREEN', 'BLUE']
            validCardList = []
            colorChoice = input("What color do you want to choose? ")
            colorChoice = colorChoice.upper()
            while colorChoice not in colorList:
                colorChoice = input("What color do you want to choose? ")
                colorChoice = colorChoice.upper()
            for card in deck_player:
                if card.startswith(colorChoice[0]):
                    validCardList.append(card)
        topCard = colorChoice[0]
        ph = topCard
    else:
        colorList = ['R', 'Y', 'G', 'B']
        randColor = randint(0,3)
        if colorList[randColor] == 'R':
            print(playerOrder[turn] + " chose Red.")
        elif colorList[randColor] == "Y":
            print(playerOrder[turn] + " chose Yellow.")
        elif colorList[randColor] == "G":
            print(playerOrder[turn] + " chose Green.")
        elif colorList[randColor] == "B":
            print(playerOrder[turn] + " chose Blue.")

# Initial setup after deck creation
deck = deck()
deck.make_deck()
card = randint(1, (len(deck.deck) - 1))
topCard = deck.deck[card]
gamestate = "in play"

def cycleMainDeck():
    global topCard, mainDeck
    newDeck = []
    newDeck.append(topCard)
    if len(deck.deck) == 0:
        deck.deck = newDeck

def playerTurn(player):
    global turn
    if player == "Player 1":
        sortdeck(player1_deck)
        validCardCheck(player1_deck)
        cardPlace()
    else:
        if player == "Bot 1":
            validCardCheck(bot1_deck, player)
        elif player == "Bot 2":
            validCardCheck(bot2_deck, player)
        elif player == "Bot 3":
            validCardCheck(bot3_deck, player)
        print("{} placed a {}".format(player, ph))
def winTest():
    global turn_deck
    for player in turn_deck:
        if player == player1_deck:
            if player1_deck == []:
                print("You win!")
                break
        if player == bot1_deck:
            if bot1_deck == []:
                print("Bot 1 wins!")
                break
        if player == bot2_deck:
            if bot2_deck == []:
                print("Bot 2 wins!")
                break
        if player == bot3_deck:
            if bot3_deck == []:
                print("Bot 3 wins!")
                break

deck.drawCard()
print("Starting card is a " + str(topCard))
turn = 0
# Handles gameplay
while gamestate == "in play":
    playerTurn(playerOrder[turn])
    if topCard == 'dF':
        drawFour(turn_deck[turn])
    elif topCard.endswith('dT'):
        drawTwo(turn_deck[turn])
    elif topCard.endswith('rev'):
        revDeck(playerOrder)
    elif topCard.endswith('skip'):
        skipCard()
    elif topCard == 'cc':
        changeColor(turn_deck[turn])
    print("Turn is increasing by 1")
    turn = (turn + 1) % 4
    cycleMainDeck()
    #time.sleep(1)
    winTest()
