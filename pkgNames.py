#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Create file with package NAMES \
        ONLY list from pip3 list -o output"
    )
    parser.add_argument("src", help="(Relative) Path to source file e.g. pkgs.txt")
    parser.add_argument("dest", help="(Relative) New location/file name e.g. upgrade.txt")
    args = parser.parse_args()
    with open(args.src, "r", newline="\n") as f:
        content = f.read()

    linesList = list(map(str.strip, iter(content.splitlines())))
    linesList = linesList[2:]
    namesList = [ln.split(" ")[0] for ln in linesList]

    with open(args.dest, "w", newline="\n") as f:
        for n in namesList:
            f.write(n + "\n")
        f.flush()


main()
