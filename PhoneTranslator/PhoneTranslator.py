import itertools
import sys

keypad = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}

filename = sys.argv[1] if len(sys.argv) > 1 else "words.txt"

keywords = []
with open(filename, 'r') as words:
    keywords = [word.upper().strip() for word in words]

def translate(*code):
    items = [keypad[key] for key in code]
    result = (''.join(a) for a in itertools.product(*items))
    result = filter(lambda s: any(v in s for v in "AEIOUY"), result)
    notable = None if not keywords else filter(lambda s: any(w in s for w in keywords), result)
    return (result, notable);

if __name__ == "__main__":
    pass