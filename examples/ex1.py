import sys

sys.path.append(".")
from efficient_args import addBaseArgs, addListArgs, parseArgs, parseCmdLineList
import argparse

if __name__ == "__main__":
    formatter = lambda prog: argparse.HelpFormatter(prog, indent_increment=4, max_help_position=80)
    parser = argparse.ArgumentParser(description="Example Command Parser", formatter_class=formatter)

    addBaseArgs(parser, addEnvironment=True)
    addListArgs(parser, required=True, itemName="Words")
    argDict = parseArgs(parser)
    print(argDict)

    words = parseCmdLineList(argDict)
    print(words)
