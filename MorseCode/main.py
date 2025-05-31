# Morse Code Dictionary for letters, digits, and some common punctuation
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Represent space between words
}

def string_to_morse(input):
    morse_code = " "
    for char in input.upper():
        if char in MORSE_CODE_DICT:
            morse_code+=MORSE_CODE_DICT[char]+' '
        else:
            morse_code+="[?]"
    return morse_code.strip()

print("STRING CONVERSION INTO MORSE_CODE")
text = input("Enter the text: ")
output = string_to_morse(text)
print(f"\nMORSE CODE:\n{output}")
