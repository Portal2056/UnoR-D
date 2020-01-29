from random import *

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
player1_deck = []
bot1_deck = []
bot2_deck = []
bot3_deck = []

# Handles sorting of decks and player order in-game
sortedDeck = []
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
    rSort = []
    ySort = []
    gSort = []
    bSort = []
    wSort = []
    num_sorted_deck = []

    #Sort by number
    for i in range(10):
        for card in deck:
            if card.endswith('_' + str(i)):
                num_sorted_deck.append(card)
    global card_types
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
def cardPlace(deck):
    global topCard
    if playerOrder[turn] == "Player 1":
        global cardChoice
        cardChoice = input("What card do you want to play? ")
        while cardChoice not in deck:
            cardChoice = input("What card do you want to play? ")
        if cardChoice in deck:
            print("You placed " + str(cardChoice) + ".")
            deck.remove(cardChoice)
            topCard = cardChoice
    else:
        validCardCheck(deck)

# Checks for valid (playable/legal) cards during a player turn
validCardList = []

def validCardCheck(deck):
    global turn
    global card
    global topCard
    validCardList = []
    for card in deck:
        if card.startswith(topCard[0]) or card.endswith(topCard[-1]) or card.endswith('cc') or card.endswith('dF'):
            validCardList.append(card)
    if playerOrder[turn] == "Player 1":
        if validCardList == []:
            print("You have no playable cards in your hand. You are forced to draw a card from the deck.")
            addCard(player1_deck)
            sortdeck(player1_deck)
        else:
            print("Valid cards in your deck are " + str(validCardList) + ".")
    elif playerOrder[turn] == "Bot 1":
        if validCardList == []:
            print("Bot 1 had no playable cards and was forced to draw.")
            addCard(deck)
            print(str(playerOrder[(turn + 1) % 4]) + ", it's your turn!")
        else:
            pickRandCard = randint(0,len(validCardList)-1)
            deck.remove(deck[pickRandCard])
            topCard = deck[pickRandCard]
    elif playerOrder[turn] == "Bot 2":
        if validCardList == []:
            print("Bot 2 had no playable cards and was forced to draw.")
            addCard(deck)
            print(str(playerOrder[(turn + 1) % 4]) + ", it's your turn!")
        else:
            pickRandCard = randint(0,len(validCardList))
            deck.remove(deck[pickRandCard])
            topCard = deck[pickRandCard]
    elif playerOrder[turn] == "Bot 3":
        if validCardList == []:
            print("Bot 3 had no playable cards and was forced to draw.")
            addCard(deck)
            print(str(playerOrder[(turn + 1) % 4]) + ", it's your turn!")
        else:
            pickRandCard = randint(0,len(validCardList))
            deck.remove(deck[pickRandCard])
            topCard = deck[pickRandCard]

# Adds card to a given deck, removing it from the mainDeck's list in doing so
def addCard(deck1):
    global card
    card = randint(1, len(deck.deck) - 1)
    deck.deck.remove(deck.deck[card])

    deck1.append(deck.deck[card])

stackCount = 0

# Special card funcs
def revDeck(deck):
    if topCard.endswith('rev'):
        playerOrder.reverse()
        turn_deck.reverse()

def skipCard():
    global turn
    if topCard.endswith('skip'):
        if turn == 3:
            turn = 0
        else:
            turn += 1

def drawTwo(deck):
    global stackCount
    global card
    global topCard
    global turn
    global deckList
    deckList = [player1_deck, bot1_deck, bot2_deck, bot3_deck]
    while topCard == 'dT':
        for card in deck:
            if card.endswith('dT'):
                deck.remove(card)
                stackCount += 2
                turn = (turn + 1) % 4
                drawTwo(deckList[turn])
    if 'dT' not in deck:
        for d in range(stackCount):
            addCard(deck)
    print(str(playerOrder[turn]) + " has to draw " + str(stackCount) + " cards.")

def drawFour(deck):
    global card
    global stackCount
    global topCard
    global turn
    global deckList
    deckList = [player1_deck, bot1_deck, bot2_deck, bot3_deck]
    while topCard == 'dF':
        for card in deck:
            if card.endswith('dF'):
                deck.remove(card)
                stackCount += 4
                turn = (turn + 1) % 4
                drawTwo(deckList[turn])
    if 'dF' not in deck:
        for d in range(stackCount):
            addCard(deck)
    print(str(playerOrder[turn]) + " has to draw " + str(stackCount) + " cards.")

def changeColor():
    global card
    global colorList
    global colorChoice
    global deck
    global topCard
    global turn
    if playerOrder[turn] == "Player 1":
        if topCard.endswith('cc'):
            colorList = ['red','yellow','green','blue']
            validCardList = []
            colorChoice = input("What color do you want to choose? ")
            colorChoice.upper()
            while colorChoice not in colorList:
                colorChoice = input("What color do you want to choose? ")
            # for card in deck:
            #     if card.startswith(colorChoice[0]):
            #         validCardList.append(card)
        topCard = colorChoice[0]
    else:
        colorList = ['R', 'Y', 'G', 'B']
        randColor = colorList[randint(0,3)]
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
    global topCard
    global mainDeck
    newDeck = []
    newDeck.append(topCard)
    if len(deck.deck) == 0:
        deck.deck = newDeck

def playerTurn():
    global turn
    if playerOrder[turn] == "Player 1":
        sortdeck(player1_deck)
        validCardCheck(player1_deck)
        cardPlace(player1_deck)
    if playerOrder[turn] == "Bot 1":
        validCardCheck(bot1_deck)
        cardPlace(bot1_deck)
        print("Bot 1 placed a " + str(ph))
    if playerOrder[turn] == "Bot 2":
        validCardCheck(bot2_deck)
        cardPlace(bot2_deck)
        print("Bot 2 placed a " + str(ph))
    if playerOrder[turn] == "Bot 3":
        validCardCheck(bot3_deck)
        cardPlace(bot3_deck)
        print("Bot 3 placed a " + str(ph))

deck.drawCard()
print("Starting card is a " + str(topCard))
turn = 0
# Handles gameplay
while gamestate == "in play":
    playerTurn()
    ph = topCard
    if topCard == 'dF':
        turn = (turn + 1) % 4
        stackCount = 4
        drawFour(turn_deck[turn])
    elif topCard.endswith('dT'):
        turn = (turn + 1) % 4
        stackCount = 2
        drawTwo(turn_deck[turn])
    elif topCard.endswith('rev'):
        revDeck(playerOrder)
    elif topCard.endswith('skip'):
        skipCard()
    elif topCard == 'cc':
        changeColor()
    turn = (turn + 1) % 4

