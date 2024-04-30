import Bio
import random

transitions = """Transition from A to T: 0.25925674605867316
Transition from A to A: 0.3199543100133451
Transition from A to G: 0.19458958177829047
Transition from A to C: 0.22619936214969125
Transition from T to T: 0.33576772541736183
Transition from T to A: 0.24765742227258897
Transition from T to C: 0.1468085329639773
Transition from T to G: 0.2697663193460719
Transition from G to G: 0.1864371772805508
Transition from G to T: 0.3399655765920826
Transition from G to A: 0.2742857142857143
Transition from G to C: 0.19931153184165232
Transition from C to C: 0.16069257690182354
Transition from C to T: 0.3800147356787622
Transition from C to A: 0.37907533615767175
Transition from C to G: 0.0802173512617425"""

transitions_dict = {'A': dict(), 'C': dict(), 'T': dict(), 'G': dict()}

for l in transitions.splitlines():
    start = l.find("Transition from ")
    target = l.find(" to ")
    prob = l.find(": ")

    start = l[start+len("Transition from ")]
    target = l[target+len(" to ")]
    prob = float(l[prob+len(": "):])
    transitions_dict[start][target] = prob



def generate_sequence(transition_probabilities, length):
    # Initialize the sequence with a random starting base
    sequence = [random.choice(list(transition_probabilities.keys()))]

    # Generate the rest of the sequence based on transition probabilities
    for _ in range(length - 1):
        current_base = sequence[-1]
        next_base_probabilities = transition_probabilities[current_base]
        next_base = random.choices(
            list(next_base_probabilities.keys()),
            weights=list(next_base_probabilities.values())
        )[0]
        sequence.append(next_base)

    return ''.join(sequence)

# Example: generate 10 sequences of length 50
num_sequences = 100
sequence_length = 50

generated_sequences = []
for _ in range(num_sequences):
    sequence = generate_sequence(transitions_dict, sequence_length)
    generated_sequences.append(sequence)

# Print generated sequences
for i, sequence in enumerate(generated_sequences, 1):
    print(f"Sequence {i}: {sequence}")
