

def create_dfa_list():
    dfa_list = []

    # DFA 1: Even number of 0s
    dfa1 = {
        'description': '1. Even number of 0s',
        'states': ['q0', 'q1'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q0', '1': 'q1'}
        },
        'start_state': 'q0',
        'accept_states': ['q0']
    }
    dfa_list.append(dfa1)

    # DFA 2: Odd number of 1s
    dfa2 = {
        'description': '2. Odd number of 1s',
        'states': ['q0', 'q1'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q0'}
        },
        'start_state': 'q0',
        'accept_states': ['q1']
    }
    dfa_list.append(dfa2)

    # DFA 3: Ends with 00
    dfa3 = {
        'description': '3. Ends with 00',
        'states': ['q0', 'q1', 'q2'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q2', '1': 'q0'}
        },
        'start_state': 'q0',
        'accept_states': ['q2']
    }
    dfa_list.append(dfa3)

    # DFA 4: Starts with 101
    dfa4 = {
        'description': '4. Starts with 101',
        'states': ['q0', 'q1', 'q2', 'q3', 'q_dead'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q_dead', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q_dead'},
            'q2': {'0': 'q_dead', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q3'},
            'q_dead': {'0': 'q_dead', '1': 'q_dead'}
        },
        'start_state': 'q0',
        'accept_states': ['q3']
    }
    dfa_list.append(dfa4)

    # DFA 5: Contains 010 as a substring
    dfa5 = {
        'description': '5. Contains 010 as a substring',
        'states': ['q0', 'q1', 'q2', 'q3'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q3', '1': 'q0'},
            'q3': {'0': 'q3', '1': 'q3'}
        },
        'start_state': 'q0',
        'accept_states': ['q3']
    }
    dfa_list.append(dfa5)

    # DFA 6: Length is a multiple of 3
    dfa6 = {
        'description': '6. Length is a multiple of 3',
        'states': ['q0', 'q1', 'q2'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q1', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q2'},
            'q2': {'0': 'q0', '1': 'q0'}
        },
        'start_state': 'q0',
        'accept_states': ['q0']
    }
    dfa_list.append(dfa6)

    # DFA 7: Exactly two 1s
    dfa7 = {
        'description': '7. Exactly two 1s',
        'states': ['q0', 'q1', 'q2', 'q3'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q3'}
        },
        'start_state': 'q0',
        'accept_states': ['q2']
    }
    dfa_list.append(dfa7)

    # DFA 8: Alternating 0s and 1s (no consecutive duplicates)
    dfa8 = {
        'description': '8. Alternating 0s and 1s (no consecutive duplicates)',
        'states': ['q0', 'q1', 'q2', 'q_dead'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q1', '1': 'q2'},
            'q1': {'0': 'q_dead', '1': 'q2'},
            'q2': {'0': 'q1', '1': 'q_dead'},
            'q_dead': {'0': 'q_dead', '1': 'q_dead'}
        },
        'start_state': 'q0',
        'accept_states': ['q0', 'q1', 'q2']
    }
    dfa_list.append(dfa8)

    # DFA 9: At least three 0s
    dfa9 = {
        'description': '9. At least three 0s',
        'states': ['q0', 'q1', 'q2', 'q3'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q1'},
            'q2': {'0': 'q3', '1': 'q2'},
            'q3': {'0': 'q3', '1': 'q3'}
        },
        'start_state': 'q0',
        'accept_states': ['q3']
    }
    dfa_list.append(dfa9)

    # DFA 10: No consecutive 1s
    dfa10 = {
        'description': '10. No consecutive 1s',
        'states': ['q0', 'q1', 'q_dead'],
        'alphabet': {'0', '1'},
        'transitions': {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q0', '1': 'q_dead'},
            'q_dead': {'0': 'q_dead', '1': 'q_dead'}
        },
        'start_state': 'q0',
        'accept_states': ['q0', 'q1']
    }
    dfa_list.append(dfa10)

    return dfa_list
