# This class is responsible for simulating DFA by indicating start_states, alphabet, transitions and accept_states
def simulate_dfa(dfa, input_str):
    current_state = dfa['start_state']
    for symbol in input_str:
        if symbol not in dfa['alphabet']:
            return False
        current_state = dfa['transitions'][current_state][symbol]

    return current_state in dfa['accept_states']
