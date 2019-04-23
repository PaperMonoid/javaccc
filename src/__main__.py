import argparse
from regex import Regex
from graph import Graph

parser = argparse.ArgumentParser(
    description="A set of tools for Java Compiler Compiler™ (JavaCC™) made in python."
)

parser.add_argument(
    "regex", metavar="r", type=str, nargs="+", help="a regular expression to compile"
)

if __name__ == "__main__":
    args = parser.parse_args()
    regex = " ".join(args.regex)
    automata = Regex(regex)
    automata_dict = automata.get_dict()
    print(automata_dict)
    graph = Graph(automata_dict.get("nodes"), automata_dict.get("edges"), "my_test")
    graph.Save()
