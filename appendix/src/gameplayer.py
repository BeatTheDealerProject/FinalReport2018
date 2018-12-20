class GamePlayer:

    def __init__(self):
        self.cards = []
        self.total = 0
        self.acetotal = 0
        self.usedace = 0
        self.burst = False
        self.naturalbj = False
        self.normalbj = False
        self.surrendeflg = False

    def initialize(self):
        self.cards = []
        self.total = 0
        self.acetotal = 0
        self.usedace = 0
        self.burst = False
        self.naturalbj = False
        self.normalbj = False
        self.surrendeflg = False

    # This function returns sum of player hand
    def totalvalue(self):
        i = 0
        self.total = 0
        self.acetotal = 0
        cardnum = len(self.cards)

        while i < cardnum:
            if self.cards[i].rank == 'A':
                self.acetotal += 1
            self.total += self.cards[i].value
            i += 1
        self.total -= 10 * self.usedace

        # jundge bust of player
        if self.total > 21:
            if self.acetotal - self.usedace > 0:
                self.total -= 10
                self.usedace += 1
                if self.total > 21:
                    self.burst = True
            else:
                self.burst = True