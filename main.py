
from dfa_creation import create_dfa_list
from dfa_visualization import visualize_dfa
from dfa_simulation import simulate_dfa


def main():
    dfa_list = create_dfa_list()
    print("Select a DFA to visualize and test:")
    for dfa in dfa_list:
        print(dfa['description'])

    while True:
        try:
            choice = int(input("\nEnter the DFA number (1-10): "))
            if choice < 1 or choice > 10:
                print("Invalid choice. Please enter a number between 1 and 10.")
                continue

            dfa = dfa_list[choice - 1]
            print(f"\nYou selected DFA: {dfa['description']}")

            # Visualize the selected DFA
            print("\nVisualizing the DFA...")
            dot = visualize_dfa(dfa)
            dot.render(f"dfa_{choice}", format='png', cleanup=True)
            print(f"DFA visualization saved as 'dfa_{choice}.png'.")

            # Test the DFA with an input string
            input_str = input("\nEnter a binary string to test the DFA: ")
            result = simulate_dfa(dfa, input_str)
            if result:
                print(f"The input string '{input_str}' is accepted by the DFA.")
            else:
                print(f"The input string '{input_str}' is rejected by the DFA.")

            cont = input("\nDo you want to test another DFA? (y/n): ").lower()
            if cont != 'y':
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    main()
