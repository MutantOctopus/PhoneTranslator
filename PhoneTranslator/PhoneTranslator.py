import itertools
import sys

keypad = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}

filename = sys.argv[1] if len(sys.argv) > 1 else "words.txt"

keywords = []
with open(filename, 'r') as words:
    keywords = [word.upper().strip() for word in words]

def translate(*code):
    vowel_check = lambda s: any(v in s for v in "AEIOUY")
    keyword_check = lambda s: any(w in s for w in keywords)
    items = [keypad[key] for key in code]
    fullresult, keyresult = itertools.tee(''.join(a) for a in itertools.product(*items))
    result = filter(vowel_check, fullresult)
    notable = None if not keywords else filter(lambda s: keyword_check(s), keyresult)
    return (result, notable);

if __name__ == "__main__":
    filename = None
    index = 0
    is_filtering = True

    def interpret(phonum):
        global index
        index += 1
        nums = [int(i.strip()) for i in phonum.split(",")]
        # Select file to output to:
        output_file = open(filename.format(digits = ''.join(str(i) for i in nums), index = str(index)), "a+") if filename\
            else sys.stdout
        # Translate and output:
        all, notable = translate(*nums)
        to_output = itertools.chain(["Translation of " + phonum], notable if is_filtering else all)
        for elem in to_output:
            print(elem, file = output_file)
        # Close files:
        if output_file != sys.stdout:
            output_file.close()

    print("Phone Translator Program: Numbers to Letters")
    while True:
        print("Select an option:")
        print("rf: Read from file")
        print("rl: Read input line")
        print("sf: Save results to named file")
        print("f: Toggle filtered or full (currently " + ("filtered" if is_filtering else "full") + ")")
        print("q: Quit")

        if filename:
            print("Printing to " + filename)
        else:
            print("Printing to standard output")

        poll = input()

        if poll == "rf":
            print("WARNING: This may take some time!")
            read_name = input("Type file name to read (Leave blank to cancel):")
            with open(read_name, "r") as r:
                for l in r:
                    try:
                        interpret(l)
                    except ValueError as ve:
                        print("Ecountered error while trying to parse; " + str(ve.args))
        elif poll == "rl":
            try:
                interpret(input("Insert line to interpret: "))
            except ValueError as ve:
                print("Encountered error trying to parse; " + str(ve.args))
        elif poll == "sf":
            print("Choose the name for the file to write to:")
            print("Leave blank to cancel file saving")
            print("Insert $d to insert the input numbers")
            print("Insert $i to insert the index of the "
                  + "current translation of this session")
            filename = input()\
                .replace("{", "{{")\
                .replace("}", "}}")\
                .replace("$d", "{digits}")\
                .replace("$i","{index}")
        elif poll == "f":
            is_filtering = not is_filtering
            print("Filtering toggled to " + "filtered" if is_filtering else "full")
        elif poll == "q":
            break
        else:
            print("{0} is not an option".format(poll))
    print("Exiting")
