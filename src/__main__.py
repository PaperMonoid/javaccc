import argparse
from regex import generate

parser = argparse.ArgumentParser(
    description="A set of tools for Java Compiler Compiler™ (JavaCC™) made in python."
)

parser.add_argument(
    "regex", metavar="r", type=str, nargs="+", help="a regular expression to compile"
)

if __name__ == "__main__":
    args = parser.parse_args()
    regex = " ".join(args.regex)
    automata = generate(regex)
    print(automata)
