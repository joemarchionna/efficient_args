import argparse


def addBaseArgs(
    parser: argparse.ArgumentParser,
    addDryRun: bool = False,
    addEnvironment: bool = False,
    environmentOptions=["prod", "test", "dev"],
    defaultEnvironmentOption="test",
):
    """
    adds base args to the parser

    Args:
        parser (argparse.ArgumentParser): the parser to add the args to
        addDryRun (bool, optional): if true, adds a 'dryrun' switch. Defaults to False
        addEnvironment (bool, optional): if true, adds a 'environment' switch. Defaults to False
        environmentOptions (list, optional): valid environment options. Defaults to ["prod", "test", "dev"]
        defaultEnvironmentOption (str, optional): default environment. Defaults to "test"
    """
    lp = parser.add_mutually_exclusive_group()

    lp.add_argument(
        "-q",
        "--quiet",
        help="Quiet, Produce Almost No Logging",
        action="store_true",
        default=False,
    )

    lp.add_argument(
        "-v",
        "--verbose",
        help="Verbose, Produce Excessive Logging",
        action="store_true",
        default=False,
    )

    if addDryRun:
        parser.add_argument(
            "-n",
            "--dryrun",
            help="No Changes, Ie, Perform A 'Dry Run'",
            action="store_true",
            default=False,
        )

    if addEnvironment:
        parser.add_argument(
            "-e",
            "--environment",
            choices=environmentOptions,
            help="Environment 'name' To Use, Default: '" + defaultEnvironmentOption + "', Options: " + ", ".join(environmentOptions),
            metavar="name",
            default=defaultEnvironmentOption,
        )


def addListArgs(parser: argparse.ArgumentParser, required: bool = False, itemName: str = "Items"):
    """
    adds a mutually exclusive group to the parser to add a list
    of items to or a file name that would be parsed for the item list

    Args:
        parser (argparse.ArgumentParser): the parser to add the group to
        required (bool, optional): if required. Defaults to False
        itemName (str, optional): the name of the objects. Defaults to "Items"
    """
    inputGrp = parser.add_mutually_exclusive_group(required=required)
    inputGrp.add_argument(
        "-l",
        "--list",
        help="{} As Space-Delimited List From The Command Line".format(itemName),
        metavar=itemName.lower(),
        type=str,
        nargs="+",
        default=[],
    )
    inputGrp.add_argument(
        "-f",
        "--file",
        help="File Path, Get {} From A File, One On Each Line".format(itemName),
        metavar="fqfn",
        type=str,
        default=None,
    )
