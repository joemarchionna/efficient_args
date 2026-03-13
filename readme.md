# efficient-args - Helper Methods For argparse

Provides some simple methods for setting up scripts / apps in a multi-environment context.

## Usage

Installation:

````bash
    pip install efficient-args
````

This library was created to be used with scripts / apps that operate in multiple environments

````python
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


    words = parseCmdLineList(argDict)
    print(words)
````

Results in the output:

````bash
    user@pc MINGW64 /efficient_args
    23:50:45 (env) $ python examples/ex1.py -f tests/itemList.txt
    {'quiet': False, 'verbose': False, 'environment': 'test', 'list': [], 'file': 'tests/itemList.txt'}
    ['x33', 'x88', 'x44']
````

## Cloning For Development

Set up a virtual environment. Once an environment is set up, activate it and add dependencies with the following:

````bash
    pip install -r requirements/dev.txt
````

The dev.txt file includes:

* BLACK, a code formatter, see notes at the bottom of this file for details
* build, which provides the support for the building of the package

### To run tests:

````bash
    python -m unittest discover -s tests/
````

### Code Formatting

Code formatting is done using BLACK. BLACK allows almost no customization to how code is formatted with the exception of line length, which has been set to 119 characters.

Use the following to bulk format files:


````bash
    black . -l 144
````

### Creating A New Release

Please do the following when making a new release, most are documented above:

1. Run tests
1. Code format
1. Be sure to update the change log and _metadata.json with version and notes
1. git add, commit, and push changes
1. run the following code to generate a wheel:

````bash
    python -m build
````
