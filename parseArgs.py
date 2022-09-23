import argparse
import sys


class ParseArgs():
    def __init__(self):
        self.args = self.arguments()

    def arguments(self):
        parser = argparse.ArgumentParser()
        # add flag params
        parser.add_argument("--option")
        args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
        return args

parser = ParseArgs()
