import itertools

keypad = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}

def translate(*code):
    items = [keypad[key] for key in code]
    result = (''.join(a) for a in itertools.product(*items))
    result = filter(lambda s: any(v in s for v in "AEIOUY"), result)
    return result;