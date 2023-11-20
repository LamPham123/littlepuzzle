def reverse_string(s):
    """Reverses the characters of the input string."""
    return s[::-1]

def remove_vowels(s):
    """Removes vowels from the input string."""
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def capitalize_alternating(s):
    """
    Capitalizes alternating characters (index 0, 2, 4, ...) of the input string,
    and converts the rest to lowercase.
    """
    return ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(s))

def string_concatenation_challenge(input_str):
    """
    Applies the three given functions in the following order:
    1. reverse_string
    2. remove_vowels
    3. capitalize_alternating
    
    Returns the final concatenated string.
    """
    # Your code here
    return capitalize_alternating(remove_vowels(reverse_string(input_str)))

input_str = "My Big is so cool and these puzzles are just a piece of cake"
result = string_concatenation_challenge(input_str)
print(result)
