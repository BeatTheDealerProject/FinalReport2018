import random
import numpy as np
import pickle
from multiprocessing import Pool

class GA:
  def __init__(self, Np, Ng, Pc, Pm, locus_num):
    self.Np = Np   #選出個体数(population number)
    self.Ng = Ng   #最大世代(generation number)
    self.Pc = Pc   #交叉率(probability of clossover)
    self.Pm = Pm   #突然変異率(probability of mutation)
    self.locus_num = locus_num  #遺伝子座
  
  def Solve(self, func):
    group_hist = list()
    self.fitnessfunc = func
    p = Pool(10)
    
    #最大世代数分計算
    for i in range(self.Ng):
      #個体ごとの適応度を計算
      evaluation = p.map(self.GetFitness, self.group)
      if i > 0:
        #エリート個体と最低評価個体の入れ替え
        low_i = np.argmin(evaluation)
        self.group[low_i] = elite
        evaluation[low_i] = elite_score
      #履歴の保存
      if i % 10 == 0:
        with open('progress{}.dat'.format(int(i/10)), 'wb') as f:
          savedata = list(zip(self.group, evaluation))
          pickle.dump(savedata,f)
      group_hist.append(self.group)
      #適応度比例選択によって親個体を選出
      fitness = [e/sum(evaluation) for e in evaluation]
      candidate = [self.Selection(self.group, fitness) for j in range(self.Np)]
      #エリート(優秀個体)の選出
      elite_i = np.argmax(evaluation)
      elite = list(self.group[elite_i])
      elite_score = evaluation[elite_i]
      #新世代の個体群
      newgroup = list() 
      #親個体の選出
      while len(newgroup) != self.Np:
        #交叉のための親を選定
        parent1 = self.Selection(self.group, fitness)
        parent2 = self.Selection(self.group, fitness)
        #交叉もしくはコピーを作成
        children = list()
        if random.random() < self.Pc:
          children = self.UniformCrossOver(parent1, parent2)
        else:
          children.append(parent1)
          children.append(parent2)
        #突然変異を適用
        for child in children:
          self.Mutation(child)
          newgroup.append(child)
      self.group = list(newgroup)
    
    with open('garesult.dat', 'wb') as f:
      pickle.dump(group_hist, f)

  def GetFitness(self, individual):
    fitness = self.fitnessfunc(individual)
    return fitness
  
  def Mutation(self, individual):
    for i in range(self.locus_num):
      if random.random() < self.Pm:
        individual[i] = '1' if individual[i] == '0' else '0'

  def CrossOver(self, parent1, parent2):
    return self.UniformCrossOver(parent1, parent2)
  
  def UniformCrossOver(self, parent1, parent2):
    child1 = list()
    child2 = list()
    mask = [0 if random.random() < 0.5 else 1 for i in range(self.locus_num)]
    for i,mb in enumerate(mask):
      if mb == 1:
        child1.append(parent2[i])
        child2.append(parent1[i])
      else:
        child1.append(parent1[i])
        child2.append(parent2[i])
    return [child1, child2]
  
  def Selection(self, group, fitness):
    return self.FitnessProportionalSelection(group, fitness)
  
  def FitnessProportionalSelection(self, group, fitness):
    choiced_index = np.random.choice([i for i in range(len(group))], p=fitness)
    candidate = group[choiced_index]
    return candidate

  def GenerateGroup(self, individual_num):
    self.group = [self.GenerateIndividual() for i in range(individual_num)]
    return

  def GenerateIndividual(self):
    individual = list()
    for i in range(self.locus_num):
      num_str = '0' if random.random() < 0.5 else '1'
      individual.append(num_str)
    return individual
