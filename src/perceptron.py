import numpy as np


class Perceptron:
    
    def __init__(self, num_inputs, activation_threshold, learn_const):
        self.num_inputs = num_inputs
        self.activation_threshold = activation_threshold
        self.learn_const = learn_const
        self.inputs = np.zeros(self.num_inputs)
        self.weights = np.random.rand(self.num_inputs)

    def __repr__(self):
        return "len inputs {}, act threshold {}, learn c {}, weights {}".format(
            self.num_inputs, self.activation_threshold, self.learn_const, self.weights
        )

    def feed_forward(self, inputs):
        return np.sum(inputs * self.weights)
    
    def activation_function(self, value):
        if value > self.activation_threshold:
            return 1
        return 0

    def activate_neuron(self, inputs):
        value = self.feed_forward(inputs)
        return self.activation_function(value)

    def train(self, inputs, target):
        attempt = self.activate_neuron(inputs)
        error = target - attempt
        self.weights += inputs * error * self.learn_const
