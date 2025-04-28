
# DFA Simulator & Visualizer

## Description:
`dfa-sim-visualizer` is a Python-based tool for simulating and visualizing Deterministic Finite Automata (DFA). It allows users to test binary strings against predefined DFAs and view the state transition diagrams in PNG format.

---

## Features

- **Predefined DFAs**: Choose from 10 different DFAs with varying properties such as even number of 0s, odd number of 1s, and more.
- **DFA Visualization**: Generates graphical representations of the selected DFA state transitions using Graphviz.
- **String Simulation**: Test binary strings against the selected DFA to check if they are accepted or rejected.
- **Interactive CLI**: Simple command-line interface for easy selection and testing of DFAs.

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ibrahimHuseynov7/dfa-state-simulator.git
    cd dfa-sim-visualizer
    ```

2. **Install dependencies**:

    Ensure you have Python 3.x installed, and then install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` includes:

    - `graphviz`: For generating DFA visualizations.
    - `pygraphviz`: Python interface for working with Graphviz.

---

## Usage

1. **Run the program**:

    ```bash
    python main.py
    ```

2. **Interact with the program**:
    - Select a DFA by entering a number between 1 and 10.
    - The program will generate a visual representation of the DFA, saved as `dfa{number}.png`.
    - Enter a binary string (composed of `0`s and `1`s) to check if it is accepted or rejected by the selected DFA.

3. **Termination and PNG Generation**:
    - Once you exit the program, a PNG file of the DFA's state diagram will be saved locally in the directory where you run the script (e.g., `dfa1.png`, `dfa2.png`, etc.). This file represents the state transition diagram of the selected DFA.

---

## DFA Descriptions

Here are the 10 predefined DFAs:

1. **Even number of 0s**
2. **Odd number of 1s**
3. **Ends with 00**
4. **Starts with 101**
5. **Contains 010 as a substring**
6. **Length is a multiple of 3**
7. **Exactly two 1s**
8. **Alternating 0s and 1s (no consecutive duplicates)**
9. **At least three 0s**
10. **No consecutive 1s**

---

## Class Descriptions

### 1. **DFA Creation (`dfa_creation.py`)**

   - **Functionality**: This module defines the creation of predefined DFAs.
   - **Main Function**: `create_dfa_list()` – Creates and returns a list of dictionaries, each containing a description and a state transition table for a particular DFA. These DFAs are predefined based on different string conditions such as "even number of 0s", "ends with 00", etc.
   - **Use**: When you run the program, this module provides the DFAs that the user can select for simulation and visualization.

### 2. **DFA Visualization (`dfa_visualization.py`)**

   - **Functionality**: This module is responsible for visualizing the DFA state transitions.
   - **Main Function**: `visualize_dfa(dfa)` – Takes a DFA dictionary as input, generates a Graphviz DOT representation of the DFA, and saves it as a PNG image. Each DFA gets saved as a file with the format `dfa{number}.png`.
   - **Use**: After selecting a DFA, this module will generate a PNG diagram showing its states and transitions.

### 3. **DFA Simulation (`dfa_simulation.py`)**

   - **Functionality**: This module handles the simulation of binary strings against the selected DFA.
   - **Main Function**: `simulate_dfa(dfa, binary_string)` – Simulates the given binary string on the DFA and checks whether the string is accepted or rejected based on the DFA’s transition rules and final states.
   - **Use**: After visualizing a DFA, this module will prompt you to enter a binary string and then determine whether the string is accepted or rejected by the selected DFA.

### 4. **Main Program (`main.py`)**

   - **Functionality**: This is the entry point of the program, where the user interacts with the tool. It coordinates the interaction between DFA selection, visualization, and simulation.
   - **Main Function**: `main()` – Prompts the user to select a DFA from the predefined list, visualizes the selected DFA, and allows the user to input binary strings to test against the DFA. It handles user input, loops, and exits the program gracefully.
   - **Use**: This is the file that you run to start the program. It loads the DFAs, displays them for the user to choose from, and enables testing and visualizations.

---

## Example

When you select DFA 1 ("Even number of 0s"):

1. The program will generate a PNG image of the DFA's state diagram, saved as `dfa1.png`.
2. You will be prompted to enter a binary string, such as `0101`.
3. The program will test the string against the DFA and tell you whether it is accepted or rejected.

---

## Future Implementations

This project is designed with flexibility in mind and has the potential for expansion. Here are some ideas for future features and improvements:

### 1. **Add More DFAs**
   - Users can add more DFAs to the system by simply defining their states, transitions, and acceptance conditions. We can create a user-friendly interface or configuration file to dynamically load new DFA definitions and simulate them without changing the core codebase.

### 2. **Convert DFAs to NFAs (Non-deterministic Finite Automata)**
   - Implement a feature that automatically converts DFAs to their NFA equivalents. This would help in understanding how deterministic automata relate to non-deterministic ones. A conversion algorithm can be added to transform the current DFA to an NFA and visualize both models.

### 3. **Context-Free Grammar (CFG) Support**
   - Introduce the ability to handle Context-Free Grammars (CFGs) and convert them to equivalent Pushdown Automata (PDA). This can allow for a deeper exploration of formal languages beyond regular languages, introducing users to more advanced automata theory.

### 4. **Enhanced Visualization**
   - Improve the graphical representation of automata by supporting more complex visual features like animation, step-by-step state transitions, or even interactive simulation where users can control the execution flow.

### 5. **Extend to Other Formal Languages**
   - Add support for other formal languages and automata, such as Turing Machines, by allowing users to define tape operations, states, and transition rules.

---

## Acknowledgements

- This project uses the **Graphviz** and **pygraphviz** libraries for visualizing state diagrams.

---
