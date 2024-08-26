import sys


def analyse(txt: str) -> dict:
    """
This function takes a string as input and returns a
dictionary containing the counts of
uppercase letters, lowercase letters,
punctuation marks, spaces, and digits within the string.
"""
    values = {'upper': 0, 'lower': 0, 'punctuation': 0,
              'spaces': 0, 'digits': 0}
    for char in txt:
        if char.isupper():
            values['upper'] += 1
        elif char.islower():
            values['lower'] += 1
        elif char.isspace():
            values['spaces'] += 1
        elif char.isdigit():
            values['digits'] += 1
        else:
            values['punctuation'] += 1
    return values


def print_analysis(data: dict, txt: str):
    """
    it allows all relevant information
    to be written with the letters in the text
    """
    print(f"The text contains {len(txt)} characters:")
    print(f"{data['upper']} upper letters")
    print(f"{data['lower']} lower letters")
    print(f"{data['punctuation']} punctuation marks")
    print(f"{data['spaces']} spaces")
    print(f"{data['digits']} digits")


def main():
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")

    else:
        try:
            assert len(sys.argv) < 3, "more than one argument"
            text = sys.argv[1]
        except AssertionError as msg:
            print(f"Assertion Error: {msg}")
            exit()

    data = analyse(text)
    print_analysis(data, text)


if __name__ == "__main__":
    main()
# space kısmında sorun var galiba
