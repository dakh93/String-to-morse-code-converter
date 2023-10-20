import sys

# Constants
MORSE_CODE_DICT = { 'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', ' ': '/'}


def translate(input):
    generated_phrase = ""
    for curr_char in list(input.upper()):
        generated_phrase = generated_phrase + " " + MORSE_CODE_DICT[curr_char]
    return generated_phrase


if __name__ == "__main__":
    # Get string input from console
    user_input = str(input("Enter sentence which you want to be translated into Morse code:"))

    try:
        translate(user_input)
    except KeyError:
        print("Entered word or sentence contains invalid characters!")
        sys.exit(1)

    final_morse_code_phrase = translate(user_input)

    print(f"Generated Morse code is : {final_morse_code_phrase}")