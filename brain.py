import numpy as np

class Brain():

    def __init__(self,inputs,outputs):

        self.nodes = []
        self.connections = []

        for i in range(0,inputs + outputs)

            if i < inputs:

                self.nodes.append(Node(i))

            else:

                self.nodes.append(Node(i))
                nodes[i].layer = 1

        for node1 in nodes:
            for node2 in nodes:

                if node2.layer > node1.layer:

                    connections.append(Connection(node1,node2))

    def engageNodes():

        for i in range(nodes.length):

            for j in range(connections.length):

                if (connections[j].nodeTo == nodes[i]):

                    nodes[i].inputSum += connections[j].output
