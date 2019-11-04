import numpy as np

class Connection():

    def __init__(self,from,to):

        self.nodeFrom = from
        self.nodeTo = to
        self.weight = np.random(-1,1)
        self.input = 0
        self.output = 0

    def setValues():

        self.input = from.output
        self.output = self.input * self.weight
