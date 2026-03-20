import sys

sys.path.append(".")
from efficient_args import FORMATTER, addBaseArgs, addListArgs, parseArgs, parseCmdLineList
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example Command Parser", formatter_class=FORMATTER)

    addBaseArgs(parser, addEnvironment=True)
    addListArgs(parser, required=True, itemName="Words")
    argDict = parseArgs(parser)
    print(argDict)

    words = parseCmdLineList(argDict)
    print(words)
