import sys


def convert(data: str) -> str:
    morse_alpha = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }
    assert data not in morse_alpha, "the arguments are bad"
    txt = ""
    for c in data:
        txt += morse_alpha.get(c)
    return txt


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        txt = sys.argv[1]
        txt = txt.upper()
        morse_text = convert(txt)
        print(morse_text)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit()


if __name__ == "__main__":
    main()
