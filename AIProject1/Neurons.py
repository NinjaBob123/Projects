from random import random
class NeuralNet:
  def __init__(self, inSize, hideSize, outSize):
    self.initialize(inSize, hideSize, outSize)
  def initialize(inParam, hideParam, outParam):
    network = []
    for neronNum in range(inParam):
      network[0].append({'input': None,
                         'weight': None,
                         'bias': None,
                         'type': 'input'})
    for neronNum in range(hideParam):
      network[1].append({'weight': None,
                         'bias': None,
                         'type': 'hidden'})
      network[1][neronNum]['weight'] = random(0.0, 10.0)
      network[1][neronNum]['bias'] = random(0.0, 10.0)

    for neronNum in range(outParam):
      network[2].append({'weight': None,
                         'bias': None,
                         'output': None,
                         'type': 'output'})
//Take out neuron specific weights
