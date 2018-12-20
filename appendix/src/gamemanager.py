class GameManager:
    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer
        self.checkdeal = True

    # judge dealer and each player
    def judge(self):
        for x in self.players:
            self.checkblackjack(x)
        self.checkblackjack(self.dealer)
        for player in self.players:
            if not player.surrendeflg:
                if player.burst == True:
                    if player.tag == "clone":
                        for i, x in enumerate(self.players):
                            if x.name == player.name:
                                self.players[i].addtotallose(player.betMoney)
                                break
                    player.addtotallose(player.betMoney)

                elif player.burst == False and self.dealer.burst == True:
                    # flag that player splits
                    spflg = False
                    for x in self.players:
                        if x.tag == "clone":
                            spflg = True

                    if player.tag == "clone":
                        for i, x in enumerate(self.players):
                            if x.name == player.name:
                                if player.naturalbj and not spflg:
                                    self.players[i].addtotalwin(player.betMoney*1.5)
                                    break
                                else:
                                    self.players[i].addtotalwin(player.betMoney)
                                    break
                    if player.naturalbj and not spflg:
                        player.addtotalwin(player.betMoney*1.5)
                    else:
                        player.addtotalwin(player.betMoney)

                elif player.total > self.dealer.total:
                    spflg = False
                    for x in self.players:
                        if player.tag=="clone":
                            spflg = True

                    if player.tag == "clone":
                        for i, x in enumerate(self.players):
                            if x.name == player.name:
                                if player.naturalbj and not spflg:
                                    self.players[i].addtotalwin(player.betMoney*1.5)
                                    break
                                else:
                                    self.players[i].addtotalwin(player.betMoney)
                                    break
                    if player.naturalbj and not spflg:
                        player.addtotalwin(player.betMoney*1.5)
                    else:
                        player.addtotalwin(player.betMoney)

                elif player.total < self.dealer.total:
                    if player.tag == "clone":
                        for i, x in enumerate(self.players):
                            if x.name == player.name:
                                self.players[i].addtotallose(player.betMoney)
                                break
                    player.addtotallose(player.betMoney)

                elif player.total == self.dealer.total:
                    if player.naturalbj and self.dealer.naturalbj:
                        if player.tag == "clone":
                            for i, x in enumerate(self.players):
                                if x.name == player.name:
                                    self.players[i].addtotaldraw()
                                    break
                        player.addtotaldraw()
                    elif player.naturalbj and self.dealer.normalbj:
                        if player.tag == "clone":
                            for i, x in enumerate(self.players):
                                if x.name == player.name:
                                    self.players[i].addtotalwin(player.betMoney * 1.5)
                                    break
                        player.addtotalwin(player.betMoney * 1.5)
                    elif player.normalbj and self.dealer.naturalbj:
                        if player.tag == "clone":
                            for i, x in enumerate(self.players):
                                if x.name == player.name:
                                    self.players[i].addtotallose(player.betMoney)
                                    break
                        player.addtotallose(player.betMoney)
                    elif player.normalbj and self.dealer.normalbj:
                        if player.tag == "clone":
                            for i, x in enumerate(self.players):
                                if x.name == player.name:
                                    self.players[i].addtotaldraw()
                                    break
                        player.addtotaldraw()
                    else:
                        if player.tag == "clone":
                            for i, x in enumerate(self.players):
                                if x.name == player.name:
                                    self.players[i].addtotaldraw()
                                    break
                        player.addtotaldraw()

    # discriminate natural or normal blackjack
    # given player or dealer as input
    def checkblackjack(self, player):
        if player.total == 21:
            if len(player.cards) == 2:
                player.naturalbj = True
            else:
                player.normalbj = True