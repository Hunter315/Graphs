#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
from graph import Graph

def main():

    graph = Graph()  # my graph instance
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_vertex('8')
    graph.add_vertex('9')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '3')
    graph.add_edge('9', '2')
    graph.add_edge('2', '3')
    graph.add_edge('4', '5')
    graph.add_edge('3', '4')
    graph.add_edge('5', '9')
    graph.add_edge('6', '7')
    graph.add_edge('7', '9')
    graph.add_edge('2', '8')

    print(graph.vertices)

    graph.bft('2')


if __name__ == '__main__':
    # TODO - parse argv
    main()
