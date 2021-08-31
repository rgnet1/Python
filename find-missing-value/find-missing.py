

# Find missing char between 2 arrays. Assume each value is unique
# EX:
# [4, 12, 9, 5, 6]
# [4, 9, 12, 6]
# Return 5

# sum the 2 lists and subtract
# possible to simplify it with xor
def find_missing(full_set, partial_set):
    return sum(full_set) - sum(partial_set)


x = [4, 12, 9, 5, 6]
y = [4, 9, 12, 6]

print(find_missing(x, y))