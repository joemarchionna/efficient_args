import argparse
import logging
import sys

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def parseArgs(parser: argparse.ArgumentParser) -> dict:
    """
    returns the args as a dict

    Args:
        parser (argparse.ArgumentParser): the argument parser

    Returns:
        dict: _description_
    """
    cmds = vars(parser.parse_args(sys.argv[1:]))
    _logger.debug("command line args: {}".format(cmds))
    return cmds


def parseCmdLineList(cmds: dict) -> list[str]:
    """
    parses the command line list (-l and -f) parameters and returns them as a single list

    Args:
        cmds (dict): arguments as a dict

    Returns:
        list[str]: the list items
    """
    if cmds.get("list", []):
        _logger.debug("Returning {} Items From cmds['list']".format(len(cmds["list"])))
        return cmds["list"]
    if cmds.get("file", None):
        _logger.debug("Returning Items From cmds['file']")
        with open(cmds["file"]) as fr:
            items = fr.readlines()
            values = []
            for x in items:
                v = x.strip()
                if v:
                    values.append(v)
            _logger.debug("Returning {} Items From cmds['file']".format(len(values)))
            return values
    _logger.debug("No Items Specified In cmds 'list' or 'file', Returning Empty List")
    return []
