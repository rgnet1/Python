# Reverse a string
# Input: input string
# Output: output string


def reverse(my_input):
    output = ""
    for c in my_input:
        output = c + output
    return output

def reverse_optimized(my_input):
    output = []
    for c in my_input:
        output.insert(0, c)
    
    return "".join(output)


print(reverse_optimized("abc"))