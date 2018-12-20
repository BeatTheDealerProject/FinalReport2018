class Dealer(GamePlayer):
    def __init__(self, deckNum):
        self.deck = Deck(deckNum)
        self.totaldealerhandlist = [0] * 6
        self.shufflenum = 10000
        self.deck.shuffle(deckNum * self.shufflenum)
        # running count
        self.IRC = 0
        super().__init__()

    # to give out card
    def dealcard(self):

        # Assumption infinity deck
        card = Card(Card.RANKS[random.randrange(13)], "spade")
        return card
        """
        # Assumption limited deck
        # HiLow
        card = self.deck.Cards[self.deck.current]
        if 2 <= card.value <= 6:
            self.IRC = self.IRC + 1
        elif 10 <= card.value <= 11:
            self.IRC = self.IRC - 1

        self.deck.current += 1
        if self.deck.current == len(self.deck.Cards):
            self.deck.current = 0
        return card
        """


    # initial give out card
    def firstdeal(self, player):
        super().__init__()
        for x in player:
            x.initialize()
        firstdeal = 2
        while firstdeal > 0:
            self.cards.append(self.dealcard())
            for x in player:
                x.cards.append(self.dealcard())
            firstdeal -= 1

    # process until sum of hand be upper 17
    def continuehit(self):
        self.totalvalue()
        while (self.total < 17):
            self.cards.append(self.dealcard())
            self.totalvalue()