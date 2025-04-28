#This class uses graphviz to visualize our DFAs
from graphviz import Digraph


def visualize_dfa(dfa):
    dot = Digraph()
    for state in dfa['states']:
        if state in dfa['accept_states']:
            dot.attr('node', shape='doublecircle')
        else:
            dot.attr('node', shape='circle')
        dot.node(state)

    dot.node('', shape='none')
    dot.edge('', dfa['start_state'])

    for from_state, transitions in dfa['transitions'].items():
        for symbol, to_state in transitions.items():
            dot.edge(from_state, to_state, label=symbol)

    return dot
