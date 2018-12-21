import numpy as np
import sys
import argparse
import json
from geneticalgorithm import GA
import BlackJackSimulator
import pprint

def simulate(individual):
  score = 1
  #戦略表の作成
  strategy = ['0' for i in range(8*10)] #hit from 4 to 11,hard hand
  strategy.extend([individual[i] for i in range(9*10)])
  strategy.extend(['1' for i in range(10)])
  strategy.extend([individual[i+90] for i in range(9*10)])
  strategy.extend(['1' for i in range(10)])
  strategy = list(np.array(list(map(lambda x: 'H' if x == '0' else 'S', strategy))).reshape(28, 10))
  #ゲームのシミュレート
  config = dict()
  config['maxbet'] = 1
  config['minbet'] = 1
  config['gamenum'] = 50000
  config['decknum'] = 1
  config['exportresult'] = False
  config['exportdebug'] = False

  result = BlackJackSimulator.main(strategy, config)
  totalwin = result[0]['totalwin']

  #連長圧縮(個体の遺伝子のみから計算)
  count = 0
  for row_i in range(18):
    before = 'B'
    for col_i in range(10):
      if not (individual[row_i*10+col_i] == before):
        count += 2
      before = individual[row_i*10+col_i]
  
  win_rate = totalwin / 50000
  complexity = count / 180

  score = win_rate - complexity + 10
  
  return score

if __name__ == '__main__':
  #コマンドライン引数についての設定
  parser = argparse.ArgumentParser(
              prog="searchbyga",
              usage="python searchbyga [simulator config file]",
              description="",
              epilog="",
              add_help=True
            )
  #GAに関する設定ファイルを指定する引数
  parser.add_argument(
      "simulatorconfigfile",
      help="The json file what configures ga simulation."
  )

  args = parser.parse_args()

  #シミュレーションの設定ファイルを読み込む
  with open(args.simulatorconfigfile, "r") as f:
    datadic = json.load(f)
    Np = datadic['population_number']
    Ng = datadic['generation_number']
    Pc = datadic['probability_crossover']
    Pm = datadic['probability_mutation']
    locus_num = datadic['locus_num']

  ga = GA(Np, Ng, Pc, Pm, locus_num)
  ga.GenerateGroup(ga.Np)
  
  for i in range(5):
    basicstrategy = list()
    basicstrategy.extend(['h','h','s','s','s','h','h','h','h','h'])
    basicstrategy.extend(['s','s','s','s','s','h','h','h','h','h'])
    basicstrategy.extend(['s','s','s','s','s','h','h','h','h','h'])
    basicstrategy.extend(['s','s','s','s','s','h','h','h','h','h'])
    basicstrategy.extend(['s','s','s','s','s','h','h','h','h','h'])
    basicstrategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    basicstrategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    basicstrategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    basicstrategy.extend(['s','s','s','s','s','s','s','s','s','s'])

    basicstrategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    basicstrategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    basicstrategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    basicstrategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    basicstrategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    basicstrategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    basicstrategy.extend(['S','S','S','S','S','S','S','h','h','S'])
    basicstrategy.extend(['S','S','S','S','S','S','S','S','S','S'])
    basicstrategy.extend(['S','S','S','S','S','S','S','S','S','S'])

    for j,x in enumerate(basicstrategy):
      basicstrategy[j] = '0' if x == 'H' or x == 'h' else '1'

    ga.group[i] = basicstrategy

  for i in range(5):
    strategy = list()
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])

    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['S','S','S','S','S','S','S','h','h','S'])
    strategy.extend(['S','S','S','S','S','S','S','S','S','S'])
    strategy.extend(['S','S','S','S','S','S','S','S','S','S'])
    
    for j,x in enumerate(strategy):
      strategy[j] = '0' if x == 'H' or x == 'h' else '1'

    ga.group[i+5] = strategy

  for i in range(5):
    strategy = list()
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])

    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['S','S','S','S','S','S','S','h','h','S'])
    strategy.extend(['S','S','S','S','S','S','S','S','S','S'])
    strategy.extend(['S','S','S','S','S','S','S','S','S','S'])

    for j,x in enumerate(strategy):
      strategy[j] = '0' if x == 'H' or x == 'h' else '1'

    ga.group[i+10] = strategy

  for i in range(5):
    strategy = list()
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])
    strategy.extend(['s','s','s','s','s','s','s','s','s','s'])

    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['h','h','h','h','h','h','h','h','h','h'])
    strategy.extend(['S','S','S','S','S','S','S','h','h','S'])
    strategy.extend(['S','S','S','S','S','S','S','S','S','S'])
    strategy.extend(['S','S','S','S','S','S','S','S','S','S'])

    for j,x in enumerate(strategy):
      strategy[j] = '0' if x == 'H' or x == 'h' else '1'

    ga.group[i+15] = strategy

  ga.Solve(simulate)
