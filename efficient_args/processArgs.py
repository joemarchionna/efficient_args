import argparse


def addWkDir(parser: argparse.ArgumentParser, defaultDir: str = "wkdir/"):
    """
    adds a working directory option

    Args:
        parser (argparse.ArgumentParser): the parser to add the arg to
        defaultDir (str, optional): the default directory path. Defaults to "wkdir/".
    """
    parser.add_argument(
        "-wd", "--workDirectory", help="Working Directory, default: '{}'".format(defaultDir), metavar="dir", type=str, default=defaultDir
    )

    """adds total message and total exception limit, set default value, set to -1 to not include specific limit"""


def addLimits(parser: argparse.ArgumentParser, defaultProcessLimit=0, defaultErrorLimit=0, itemName: str = "Item"):
    """
    adds process and error limit switches to the parser

    Args:
        parser (argparse.ArgumentParser): the parser to add the args to
        defaultProcessLimit (int, optional): default process limit. Defaults to 0 (unlimited), set to -1 to not include limit
        defaultErrorLimit (int, optional): default error limit. Defaults to 0 (unlimited), set to -1 to not include limit
        itemName (str, optional): Process Object Name, Used In Help Description. Defaults to "Item"
    """
    if defaultProcessLimit >= 0:
        parser.add_argument(
            "-pl",
            "--processLimit",
            help="Process Limit, Maximum Number of {}s To Process, Set To 0 For Unlimited, Default: {}".format(itemName, defaultProcessLimit),
            metavar="limit",
            type=int,
            default=defaultProcessLimit,
        )

    if defaultErrorLimit >= 0:
        parser.add_argument(
            "-xl",
            "--errorLimit",
            help="Error Limit, App Stops If Error Count Reaches Limit, Set To 0 For Unlimited, Default: {}".format(defaultErrorLimit),
            metavar="limit",
            type=int,
            default=defaultErrorLimit,
        )
