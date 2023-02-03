import string

# Defining the caesar cipher function
def caesar(text, shift, alp):
    
    # Defining the shifted alphabet function
    def shift_alphabet(alphabet):
        
        # Starts at the position of the shift value and ends at the end of the string length
        return alphabet[shift:] + alphabet[:shift]

    # Mapping the shift_alphabet function onto the list of alphabets
    shift_alphabet = tuple(map(shift_alphabet, alp))

    # Joining the individual alps
    final_alphabet = ''.join(alp)

    # Joining the shifted alphabets
    final_shift_alphabet = ''.join(shift_alphabet)

    # Translation table meant for the final string of letters
    final_text = str.maketrans(final_alphabet, final_shift_alphabet)
    
    # Returning the text
    return text.translate(final_text)

# Input validation for the text and text input

print("Enter your text (letters only): ")
user_text = input()
if str.isalpha(user_text) is True:
    print(caesar(user_text, 3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
else:
    print("Please enter letters only.")
