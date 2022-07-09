def reverse_text(text):
    index = 0
    n = len(text)
    while index < n:
        yield text[n - index - 1]
        index += 1

