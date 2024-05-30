from util import valid_sequences, operator

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
valid_sequences(10)

# Question 3: For n > 6 and even, how many valid sequences can be achieved by the data operator?
# As there are 8 valid sequences for all valid n's, we have 6 achievable sequences
# The only sequences we cannot achieve are those which have both odd and even tokens decreasing
# This is because to get the decreasing token set (odd or even), you must pass that full set* into storage
#   *except the last digit, as this becomes the leading digit in the would-be achievable sequence
# It is then impossible to construct ...1...2 or ...2...1, as we cannot inject values between 1 and 2 in storage
operator(6)  # TODO :: operator(8)

# Question 4: For n >= 9 and multiple of 3, justify how many 3-valid sequences of length n there are
# 3-valid sequences are those of the form A B C, where odd even is replaced with 3k 3k+1 3k+2
# Again we have increasing decreasing, plus ordering
# We have 2 combinations of each token set for inc dec, 2 x 2 x 2 (8)
# Also, we have 3! ways of ordering our 3 elements: 3 x 2 x 1 (6)
# Therefore, there are 48 3-valid sequences

# Question 5:

