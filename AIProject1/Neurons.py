import random

class NetGen:
    def __init__(self, inSize, hideSize, hideWidth, outSize):
        self.initialize(inSize, hideSize, hideWidth, outSize)

    def initialize(self, inParam, hideParam, width, outParam):
        # Initialize network neurons
        networkNeurons = [[], []]
        for _ in range(width):
            networkNeurons.append([])

        print("Neurons before population:", networkNeurons)

        # Add input neurons
        for neuronNum in range(inParam):
            networkNeurons[0].append({
                'bias': random.random() + random.randint(-3, 3),
                'type': 'input'
            })

        # Add hidden neurons
        for layer in range(width):
            for neuronNum in range(hideParam):
                neuron = {
                    'bias': None,
                    'type': 'hidden'
                }
                neuron['bias'] = random.random() + random.randint(-3, 3)
                networkNeurons[layer + 1].append(neuron)

        # Add output neurons
        for neuronNum in range(outParam):
            networkNeurons[-1].append({
                'bias': random.random() + random.randint(-3, 3),
                'type': 'output'
            })

        print("Neurons after population:", networkNeurons)

        # Initialize network connections
        networkConnections = [[], []]
        for _ in range(width):
            networkConnections.append([])

        # Create connections from input to hidden neurons
        for connection in range(inParam):
            for neuron in range(len(networkNeurons[1])):
                networkConnections[0].append({
                    'from': f'i{connection}',
                    'to': f'h{neuron}',
                    'val': random.random() + random.randint(-1, 3)
                })

        # Create connections from hidden neurons to output neurons
        for layer in range(width):
            if width > 1:
                for neuron in range(len(networkNeurons[layer + 1])):
                    if layer == width - 1:
                        for outNeuronNum in range(len(networkNeurons[-1])):
                            networkConnections[layer + 1].append({
                                'from': f'h{neuron}',
                                'to': f'o{outNeuronNum}',
                                'val': random.random() + random.randint(-1, 3)
                            })
            # Create connection from hidden neurons to next hidden layer
                else:
                  for inNeuron in range(len(networkNeurons[layer + 1])):
                      for outNeuron in range(len(networkNeurons[layer + 2])):
                          networkConnections[layer + 1].append({
                              'from': f'h{inNeuron}',
                              'to': f'h{outNeuron}',
                              'val': random.random() + random.randint(-1, 3)})
              

        print("Network connections:", networkConnections)
        network = {'neurons': networkNeurons,
                   'connections': networkConnections}
        return network
def feedForward(network: dict, inputs: list[float]):
    networkNeurons = network['neurons']
    networkConnections = network['connections']
    inNeurons = networkNeurons[0]
    if len(input) == len(networkNeurons[0]):
        layerCount = 0
        newInput = []
        for layer in networkNeurons:
            for inNeuron in networkNeurons[layer]:
                for outNeuron in networkNeurons[layer + 1]:
                    inBias = inNeuron['bias']
                    connect = networkConnections[layer][#connection] #finish
                    input = inputs[layerCount]
                    
                    layerCount += 1
            inputs = newInput
            newInput = []
# Example usage
#net = NetGen(4, 1, 4, 1)
