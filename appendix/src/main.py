def main(strategy):
    # create player instance
    p1 = Player("player1")

    # add player who joins game
    players = [p1]

    # create dealer instance
    # the argument expresses deck num used in game
    dealer = Dealer(6)

    # this variable expresses cutcard
    cutcard = len(dealer.deck.Cards) / 2

    totalGameNum = 40
    remainingGameNum = 0

    minbet = 10

    maxbet = 10000

    trial = 50000
    trialNum = trial

    split_strategy = [["H", "H", "P", "P", "P", "P", "H", "H", "H", "H"],  # 2,2
                      ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],  # 3,3
                      ["H", "H", "H", "P", "P", "H", "H", "H", "H", "H"],  # 4,4
                      ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],  # 5,5
                      ["P", "P", "P", "P", "P", "H", "H", "H", "H", "H"],  # 6,6
                      ["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],  # 7,7
                      ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],  # 8,8
                      ["P", "P", "P", "P", "P", "S", "P", "P", "S", "S"],  # 9,9
                      ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # 10,10
                      ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"]  # A,A
                      ]

    while True:
        # main loop
        remainingGameNum = totalGameNum
        dealer.deck.shuffle(dealer.shufflenum)
        players[0].money = 1000
        dealer.IRC = 0
        if trialNum \% 100 == 0:
            print(trialNum)

        while True:
            if remainingGameNum \% 100 == 0:
                print(remainingGameNum)

            # ゲームを始める前にデッキの中からカットカードが出てきているかを確認し、出てきていれば、デッキをシャッフルする
            """
            # 有限デックの際のシャッフルを行うタイミングの記述
            if dealer.deck.current > cutcard:
                dealer.deck.shuffle(dealer.shufflenum)
                dealer.IRC = -20
            """

            # ランニングカウントによって賭け額を変化させる
            # 今回はHigh-Low法を適用している
            rc = 1
            if dealer.IRC <= 1:
                rc = 1
            else:
                rc = dealer.IRC

            if players[0].money == 0:
                money_list.append(None)
                card_num_list.append(None)

                # ループの処理
                remainingGameNum -= 1
                if remainingGameNum <= 0:
                    break

                # 各プレイヤーのベット
                for player in players:
                    if player.money < minbet * rc:
                        player.bet(player.money)
                    else:
                        player.bet(minbet * rc)

                # 参加プレイヤーの初期化を実行後、ディーラーが各プレイヤー（自身含む）に初期カードを配る
                dealer.firstdeal(players)

                # 各プレイヤーの点数を更新
                for player in players:
                    player.totalvalue()

                # サレンダーの回数を記録する
                surrenderCounter = 0

                # スプリットの回数とダブルダウンの回数を記録する
                spCounter = 0
                ddCounter = 0

                # スプリットするかどうかを確認する
                for i, player in enumerate(players):
                    if player.cards[0].rank == player.cards[1].rank:
                        usermessage = split_strategy[player.cards[0].value - 2][dealer.cards[0].value - 2]
                        if (usermessage == 'P' or usermessage == 'p') and player.money > 2 * player.betMoney:
                            # プレイヤーのクローンを作成し、ゲームに参加するプレイヤーとして追加登録する
                            playerClone = Player(player.name,money=player.money - player.betMoney, betMoney=player.betMoney, tag="clone")
                            players.insert(i + 1, playerClone)
                            spCounter += 1

                            # クローンにプレイヤーが所持しているカードを一枚渡す
                            playerClone.dealedcard(player.cards[1])
                            del player.cards[1]

                            # 使用済みAの数を初期化する
                            player.usedace = 0
                            playerClone.usedace = 0

                            # プレイヤーとクローンにカードを配り直す
                            player.dealedcard(dealer.dealcard())
                            playerClone.dealedcard(dealer.dealcard())

                for player in players:
                    if player.tag == "clone":
                        players[0].totalsplit += 1


                # 各プレイヤーに対して選択肢を提示する
                for player in players:
                    while True:
                        # プレイヤーの選択はベーシックストラテジーに沿って行われるものとする
                        # プレイヤーの手札にA(11)が残っている場合
                        if player.acetotal - player.usedace > 0:
                            usermessage = strategy[player.total + 6][dealer.cards[0].value - 2]
                        # プレイヤーの手札にA(11)が残っていない場合
                        else:
                            usermessage = strategy[player.total - 4][dealer.cards[0].value - 2]

                        # 一定条件下でプレイヤーが戦略を間違える際の処理


                        # プレイヤーの選択による行動の分岐を記述
                        # プレイヤーがヒットを選択した場合
                        if usermessage == 'H' or usermessage == 'h':
                            player.hit(dealer)
                            if player.burst:
                                break

                        # プレイヤーがスタンドを選択した場合
                        elif usermessage == 'S' or usermessage == 's':
                            player.stand()
                            break

                        # プレイヤーがダブルダウンを選択した場合
                        elif usermessage == 'D' or usermessage == 'd':
                            if players[0].money -spCounter*players[0].betMoney - ddCounter*players[0].betMoney > player.betMoney * 2:
                                # ヒット後にはダブルダウンの選択不可
                                if len(player.cards) == 2:
                                    player.doubledown(dealer)
                                    ddCounter += 1
                                    break
                                else:
                                    player.hit(dealer)
                                    if player.burst:
                                        break
                            else:
                                player.hit(dealer)
                                if player.burst:
                                    break

                        # プレイヤーがサレンダーを選択した場合
                        elif usermessage == "R" or usermessage == "r":
                            # ヒット後にはサレンダーの選択不可
                            if len(player.cards) == 2:
                                player.surrender()
                                if player.tag == "clone":
                                   players[0].totalsurrender += 1
                                surrenderCounter += 1
                                break
                            else:
                                player.hit(dealer)
                                if player.burst:
                                    break

                # ディーラーは17を超えるまでヒットを続ける
                dealer.continuehit()

                # GameManagerの初期化
                gamemanager: GameManager = GameManager(players, dealer)

                # 勝敗を判定する
                gamemanager.judge()

                # クローンを削除する
                while True:
                    cloneflg = False
                    for i, player in enumerate(players):
                        if player.tag == "clone":
                            del player
                            del players[i]
                            cloneflg = True
                    if not cloneflg:
                        break

                # ループの処理
                remainingGameNum -= 1
                if remainingGameNum <= 0:
                    break
        trialNum -= 1