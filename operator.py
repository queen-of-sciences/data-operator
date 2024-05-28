"""
    OPERATOR
    - A data operator is receiving tokens one by one through an input channel
    - The data operator will receive a total of n tokens, where n >= 6
        - These are numbered as 1, 2,...,n
    - The data operator is required to pass these tokens to the output channel
    - However they must do so using a valid sequence
        - A valid sequence is one where:
            - All the odd tokens appear first, followed by the even tokens
                - Or the other way round; furthermore
            - All the odd tokens must appear in either increasing or decreasing order
                - Likewise all the even tokens must appear in increasing or decreasing order
    - All valid sequences for n = 6 are listed below:
        - 135246 135642 531246 531642 246135 246531 642135 642531
    - The data operator has a storage unit that can hold a sequence
        - It perform the following operations as they receive the tokens one by one:
            - pass : Input token goes straight to the output channel.
            - pop : Instead of using a token from the input, the token from the right end of the
                    storage unit is removed (provided one exists) and sent to the output channel.
            - pushL : Input token is pushed in at the left end of the storage unit.
            - pushR : Input token is pushed in at the right end of the storage unit.
    - As an illustrative example, when n = 6, the storage and output channel are shown
        for the following sequence of operations, which results in the valid output sequence 1 3 5 6 4 2.

        Input Token | Operation | Storage | Output
        ────────────────────────────────────────────
         1         | pass      | []       | 1
         2         | pushR     | [2]      | 1
         3         | pass      | [2]      | 1 3
         4         | pushR     | [2 4]    | 1 3
         5         | pass      | [2 4]    | 1 3 5
         6         | pass      | [2 4]    | 1 3 5 6
                   | pop       | [2]      | 1 3 5 6 4
                   | pop       | []       | 1 3 5 6 4 2

"""

# Question 1: For n = 6, which valid sequences can the data operator achieve?
# 642531 & 531642 are not 'achievable'; could be something to do with down:down, no way to inject between 1 and 2

# Question 2: For n > 6 and even, how many valid sequences are there?
# 8 :: bc 2 (odd, then even) x 2 (even, then odd) x 2 (inc vs dec)

# Question 3: For n >= 6 and even, how many valid sequences can be achieved by the data operator?
# 8 :: Still 6, proof by exhaustion:
# ODD INC, EVEN INC (ex: 135246) :
# EVEN INC, ODD INC (ex: 246135) :
# ODD INC, EVEN DEC (ex: 135642) :
# ODD DEC, EVEN INC (ex: 531246) :
# EVEN INC, ODD DEC (ex: 246531) :
# EVEN DEC, ODD INC (ex: 642135) :
# --
# ODD DEC, EVEN DEC (ex: 531642) :
# EVEN DEC, ODD DEC (ex: 642531) :
# TODO



