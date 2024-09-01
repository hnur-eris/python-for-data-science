import sys
from ft_filter import ft_filter


def handle_error():
    """
    for handling anomali stuaiton
    """
    assert len(sys.argv) == 3, "the arguments are bad"
    assert sys.argv[1].lstrip("-").isnumeric() == 0, "the arguments are bad"


def main():
    try:
        handle_error()
        txt = sys.argv[1]
        number = int(sys.argv[2])
        words = txt.split()
        # filtered_words = list(filter(lambda x: len(x) > number, words))
        filtered_words = list(ft_filter(lambda x: len(x) > number, words))
        print(filtered_words)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit()


if __name__ == '__main__':
    main()
