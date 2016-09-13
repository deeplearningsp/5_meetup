import numpy as np
from sklearn.metrics import mean_squared_error

class Perceptron:
    
    def __init__(self, num_inputs, activation_threshold, target):
        self.num_inputs = num_inputs
        self.activation_threshold = activation_threshold
        self.target = target
        self.inputs = np.zeros(self.num_inputs)
        self.weights = np.random.rand(self.num_inputs)

    def feed_forward(self, inputs):
        return np.sum(inputs * self.weights)
    
    def activate_function(self, value):
        if value > self.activation_threshold:
            return 1
        return 0

    def activate_neuron(self, inputs):
        value = self.feed_forward(inputs)
        return self.activate_function(value)

    def train(self, inputs):
        attempt = self.activate_neuron(inputs)
        error = self.target - attempt
        self.weights += inputs * error * learn_const
        
