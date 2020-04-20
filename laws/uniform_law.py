def uniform_pdf(x, a, b):
    return [ 1/(b-a) if a <= x <= b else 0 for x in x]
