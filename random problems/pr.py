from itertools import combinations

# Define the outcomes and their probabilities
outcomes = [1/10, 2/5, 1/5, 1/10, 1/10, 1/10]

# Find all subsets of outcomes whose sum is 1/3
valid_subsets = []
for r in range(1, len(outcomes) + 1):
    for subset in combinations(outcomes, r):
        if sum(subset) == 1/2:
            valid_subsets.append(subset)

# Print the valid subsets
for subset in valid_subsets:
    print(subset)
