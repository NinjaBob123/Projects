from Neurons import *

class NeuralNet:
  def __init__(self, inSize, hideSize, hideWidth, outSize):
    self.network = NetGen(inSize, hideSize, hideWidth, outSize)
    
