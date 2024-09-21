# 60 bu progress bar uzunluğu istersen değiştir
def ft_tqdm(lst: range) -> None:
    """
    I rewrote the function that prints the progress bar in Python myself.
    """
    length = len(lst)
    for i, item in enumerate(lst, start=1):
        percent = (i / length) * 100
        filled_len = int(60 * i // length)
        bar = '=' * filled_len + '>' + '-' * (60 - filled_len - 1)
        print(f"\r{percent:3.0f}%|[{bar}]| {i}/{length}", end="")

        yield item
