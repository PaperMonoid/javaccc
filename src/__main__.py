import argparse
import csv
import os.path
import time
from regex import Regex
from graph import Graph


parser = argparse.ArgumentParser(
    description="A set of tools for Java Compiler Compiler™ (JavaCC™) made in python."
)

parser.add_argument("-i", "--input-file", type=str, help="an input csv file")

parser.add_argument("-o", "--output-dir", type=str, help="an output directory")


def save_automata(regex, name, output_dir):
    automata = Regex(regex)
    automata_dict = automata.get_dict()
    graph = Graph(
        automata_dict.get("nodes"), automata_dict.get("edges"), name, output_dir
    )
    graph.Save()


if __name__ == "__main__":
    args = parser.parse_args()
    input_file = args.input_file
    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    lines = 0
    print("starting process...")
    start_time = time.time()
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for _ in reader:
            lines = lines + 1
    print("found {0} lines".format(lines))
    count = 0
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for [name, regex] in reader:
            save_automata(regex, name, output_dir)
            count = count + 1
            print("done {0}/{1}".format(count, lines))
    elapsed_time = time.time() - start_time
    print("process finished!")
    print(
        "elapsed time: {0}".format(
            time.strftime(
                "%H hours, %M minutes and %S seconds", time.gmtime(elapsed_time)
            )
        )
    )
