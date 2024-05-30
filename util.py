
def valid_sequences(n):
    # Sequences are valid for n, where n is even and >= 6, and:
    sequences = []
    elements = range(n+1)
    base = list(elements)[1:]

    # All odds tokens are decreasing or increasing
    increasing_odds = base[0::2]
    decreasing_odds = increasing_odds[::-1]

    # All even tokens are decreasing or increasing
    increasing_evens = base[1::2]
    decreasing_evens = increasing_evens[::-1]

    # All odd tokens appear first, followed by even tokens
    sequences.append(increasing_odds + increasing_evens)
    sequences.append(increasing_odds + decreasing_evens)
    sequences.append(decreasing_odds + increasing_evens)
    sequences.append(decreasing_odds + decreasing_evens)

    # All even tokens appear first, followed by odd tokens
    sequences.append(increasing_evens + increasing_odds)
    sequences.append(increasing_evens + decreasing_odds)
    sequences.append(decreasing_evens + increasing_odds)
    sequences.append(decreasing_evens + decreasing_odds)

    print(sequences)
    print(len(sequences))

    return sequences


def operator(n):
    sequences = valid_sequences(n)

    # Remove non-achievable sequences
    for sequence in sequences:
        # for a given sequence, try to build it from 1...n using the operations
        # ex: 123456 -> ...

        # test sequence; if it fails, del sequence
        print(sequence)
