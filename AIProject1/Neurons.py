from random import random
class NeuralNet:
  def __init__(self, inSize, hideSize, hideWidth, outSize):
    self.initialize(inSize, hideSize, hideWidth, outSize)
  def initialize(inParam, hideParam, width, outParam):
    networkNeurons = []
    for layer in range(width):
      networkNeurons.append([])
    for neronNum in range(inParam):
      network[0].append({'input': None,
                         'bias': None,
                         'type': 'input'})
    for layer in range(width):
      for neronNum in range(hideParam):
        network[layer + 1].append({'bias': None,
                                   'type': 'hidden'})
        network[layer + 1[neronNum]['bias'] = random(0.0, 10.0)

    for neronNum in range(outParam):
      network[2].append({'bias': None,
                         'output': None,
                         'type': 'output'})
    networkConnections = []
    for layer in networkNeurons
