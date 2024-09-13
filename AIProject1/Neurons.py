import random

class NeuralNet:
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
                'input': None,
                'bias': None,
                'type': 'input'
            })

        # Add hidden neurons
        for layer in range(width):
            for neuronNum in range(hideParam):
                neuron = {
                    'bias': None,
                    'type': 'hidden'
                }
                neuron['bias'] = random.random() + random.randint(0, 3)
                networkNeurons[layer + 1].append(neuron)

        # Add output neurons
        for neuronNum in range(outParam):
            networkNeurons[-1].append({
                'bias': None,
                'output': None,
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
                    'val': random.random() + random.randint(0, 3)
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
                                'val': random.random() + random.randint(0, 3)
                            })
            # Create connection from hidden neurons to next hidden layer
            else:
              for inNeuron in range(len(networkNeurons[layer + 1])):
                  for outNeuron in range(len(networkNeurons[layer + 2])):
                      networkConnections[layer + 1].append({
                          'from': f'h{inNeuron}',
                          'to': f'h{outNeuron}',
                          'val': random.random() + random.randint(0, 3)
              

        print("Network connections:", networkConnections)

# Example usage
net = NeuralNet(4, 1, 4, 1)
