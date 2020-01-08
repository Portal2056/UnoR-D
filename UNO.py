from random import *
import time

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
       self.d2 = color + 'd2'
       self.skip = color + 'skip'
       self.reverse = color + 'rev'
       if deck2 == 1:
           self.list = [self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,
                       self.d2,self.skip,self.reverse]
       else:
           self.list = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,
                        self.nine, self.d2,self.skip,self.reverse]

class wild:
   def __init__(self):
       self.d4 = 'd4'
       self.cc = 'cc'
       self.list = [self.d4, self.cc] * 4


r = color(color='R_')
y = color(color='Y_')
g = color(color='G_')
b = color(color='B_')
r2 = color(color='R_',deck2=1)
y2 = color(color='Y_',deck2=1)
g2 = color(color='G_',deck2=1)
b2 = color(color='B_',deck2=1)
wild = wild()

player1_deck = []
bot1_deck = []
bot2_deck = []
bot3_deck = []

sortedDeck = []
playerOrder = ["player1","bot1","bot2","bot3"]
topCard = 'blank'

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

    def drawCard(self):
        global topCard
        card = randint(1, len(deck.deck) - 1)
        topCard = self.deck[card]
        self.deck.__delitem__(card)


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
    card_types = ['cc', 'd2', 'd4', 'rev', 'skip']
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
        if card.startswith('cc') or card.startswith('d4'):
            wSort.append(card)
    global sortedDeck
    sortedDeck = rSort + ySort + gSort + bSort + wSort
    print(sortedDeck)

def cardPlace(deck):
    if playerOrder[turn] == "player1":
        global cardChoice
        cardChoice = input("What card do you want to play? ")
        if cardChoice in deck:
            print("You placed " + str(cardChoice) + ".")
            deck.remove(cardChoice)
            topCard = cardChoice

validCardList = []

def validCardCheck(deck):
    validCardList = []
    for card in deck:
        if card.startswith(topCard[0]) or card.endswith(topCard[-1]) or card.endswith('cc') or card.endswith('d4'):
            validCardList.append(card)

    if validCardList == []:
        print("You have no playable cards in your hand. You are forced to draw a card from the deck.")
    else:
        print("Valid cards in your deck are " + str(validCardList) + ".")

def addCard(deck):
    self.deck.remove(card)
    deck.append(card)

global stackCount
stackCount = 0

def specialCardRules(deck):
    for card in deck:

        if card.endswith('rev'):
            playerOrder.reverse()

        elif card.endswith('skip'):
            if playerOrder[turn] == 3:
                playerOrder[turn] = 1
            else:
                playerOrder[turn] += 1

        elif card.endswith('d2'):
            for card in ((playerOrder[turn] + 1) % 4):
                if card.endswith('d2') in deck:
                    validCardList = []
                    validCardList.append(card)
                    if cardChoice in validCardList:
                        stackCount += 2
                    else:
                        playerOrder = ((playerOrder + 1) % 4)
                        for d in range(stackCount):
                            pass

        elif card.endswith('d4'):
            for card in ((playerOrder[turn] + 1) % 4):
                if card.endswith('d4'):
                    stackCount += 4
                    for d in range(stackCount):
                        pass

        elif card.endswith('cc'):
            pass

deck = deck()
deck.make_deck()
sortdeck(player1_deck)
turn = 0
gamestate = "in play"

topCard = 'Y_skip'

print("The current top card is a " + str(topCard) + ".")

validCardCheck(player1_deck)

while gamestate == "in play":
    # deck.drawCard()
    # print(topCard)
    pass