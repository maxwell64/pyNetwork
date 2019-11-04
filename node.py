import numpy as np

class Node():

    def __init__(self,index):

        self.inputSum = 0
        self.output = 0
        self.index = index
        self.layer = 0

    def sigmoid(input):

        return (1/1 + np.exp(-input))

    def engage():

        self.output = sigmoid(self.inputSum)
