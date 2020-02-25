from random import *
import time
# Creates numbers and basic identities of specal cards
sleepTime = int(input("Enter a time scale: "))
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
def sortdeck(deck, print_deck=0):
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
    if print_deck == 0:
        print('Your deck is: {}'.format(sortedDeck))
        time.sleep(.5 * sleepTime)

# Creates a function to place cards
def cardPlace():
    global ph, topCard, cardChoice, player1_deck
    time.sleep(.5 * sleepTime)
    cardChoice = input("What card do you want to play? ")
    if validCardList != []:
        while cardChoice not in validCardList:
            cardChoice = input("What card do you want to play? ")
            print(validCardList)
    if cardChoice in validCardList:
        print("You placed a " + str(cardChoice) + ".")
        time.sleep(.2 * sleepTime)
        player1_deck.remove(cardChoice)
        topCard = cardChoice
        validCardList.remove(cardChoice)


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
            time.sleep(.2 * sleepTime)
            addCard(player1_deck)
            sortdeck(player1_deck, 0)
            for card in hand:
                if card.startswith(topCard[0]) or card.endswith(topCard[-1]) or card.endswith('cc') or card.endswith('dF'):
                    validCardList.append(card)
            if validCardList != []:
                print("Valid cards in your deck are {}.".format(validCardList))
                time.sleep(.5 * sleepTime)
                cardPlace()
            else:
                print("You did not draw a playable card.")
                time.sleep(.2 * sleepTime)

        else:
            print("Valid cards in your deck are {}.".format(validCardList))
            time.sleep(.2 * sleepTime)
    else:
        if validCardList == []:
            print("{} had no playable cards ad was forced to draw.".format(bot))
            time.sleep(.2 * sleepTime)
            addCard(hand)
            if reversed:
                print(str(playerOrder[(turn - 1) % 4]) + ", it's your turn!")
                time.sleep(.2 * sleepTime)
            else:
                print(str(playerOrder[(turn + 1) % 4]) + ", it's your turn!")
                time.sleep(.2 * sleepTime)
            #skipCard()
        else:
            pickRandCard = randint(0,len(validCardList)-1)
            topCard = validCardList[pickRandCard]
            hand.remove(validCardList[pickRandCard])
    ph = topCard

# Adds card to a given deck, removing it from the mainDeck's list in doing so
def addCard(deck1):
    card = randint(0, len(deck.deck) - 1)
    deck1.append(deck.deck[card])
    deck.deck.remove(deck.deck[card])

stackCount = 0
reversed = 0

def skipCard():
    global turn
    if reversed:
        turn = (turn - 1) % 4
    else:
        turn = (turn + 1) % 4
def revDeck():
    global reversed
    if reversed == 0:
        reversed = 1
    else:
        reversed = 0

def drawTwo(deck):
    if reversed:
        turntemp = (turn - 1) % 4
    else:
        turntemp = (turn + 1) % 4
    for d in range(2):
        addCard(turn_deck[turntemp])
    print(str(playerOrder[turntemp]) + " has to draw 2 cards.")
    skipCard()
    time.sleep(.2 * sleepTime)

def drawFour(deck):
    global card, topCard, turn
    changeColor(deck)
    if reversed:
        turntemp = (turn - 1) % 4
    else:
        turntemp = (turn + 1) % 4
    for d in range(4):
        addCard(turn_deck[turntemp])
    print(str(playerOrder[turntemp]) + " has to draw 4 cards.")
    time.sleep(.2 * sleepTime)
    skipCard()

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
        colorList = ['RED', 'YELLOW', 'GREEN', 'BLUE']
        randColor = randint(0,3)
        print(playerOrder[turn] + " chose {}".format(colorList[randColor].capitalize()))
        time.sleep(.2 * sleepTime)
        topCard = colorList[randColor]
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
        if validCardList != []:
            cardPlace()
    else:
        if player == "Bot 1":
            validCardCheck(bot1_deck, player)
        elif player == "Bot 2":
            validCardCheck(bot2_deck, player)
        elif player == "Bot 3":
            validCardCheck(bot3_deck, player)
        if validCardList != []:
            print("{} placed a {}".format(player, ph))
            time.sleep(.2 * sleepTime)

def winTest():
    global turn_deck
    for player in turn_deck:
        if player == player1_deck:
            if player1_deck == []:
                print("You win!")
                exit()
        if player == bot1_deck:
            if bot1_deck == []:
                print("Bot 1 wins!")
                exit()
        if player == bot2_deck:
            if bot2_deck == []:
                print("Bot 2 wins!")
                exit()
        if player == bot3_deck:
            if bot3_deck == []:
                print("Bot 3 wins!")
                exit()

botDeckList = [bot1_deck, bot2_deck, bot3_deck]
botNames = ['Bot 1', 'Bot 2', 'Bot 3']
deck.drawCard()
print("Starting card is a " + str(topCard))
time.sleep(.5 * sleepTime)
turn = 0
# Handles gameplay
while gamestate == "in play":
    for counter, bot in enumerate(botNames):
        print('{} has {} cards.'.format(bot, len(botDeckList[counter])), end=' ')
        time.sleep(.5 * sleepTime)
    time.sleep(.5 * sleepTime)
    print('')
    playerTurn(playerOrder[turn])
    if topCard == 'dF':
        drawFour(turn_deck[turn])
    elif topCard.endswith('dT'):
        drawTwo(turn_deck[turn])
    elif topCard.endswith('rev'):
        revDeck()
    elif topCard.endswith('skip'):
        skipCard()
    elif topCard == 'cc':
        changeColor(turn_deck[turn])
    skipCard()
    cycleMainDeck()
    print('')
    if playerOrder[turn] != "Player 1":
        print('Thinking', end='')
        for i in range(2):
            time.sleep(.5 * sleepTime)
            print('.', end='')
        print('.')
        time.sleep(.5 * sleepTime)
    winTest()