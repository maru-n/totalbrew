#!/usr/bin/python
# encoding: UTF-8

import sys
import subprocess

if __name__ == '__main__':
    args = sys.argv

    if len(args) == 1:
        print "usage: totalbrew brew"
        sys.exit()

    if args[1] == "brew":
        command = ["brew"] + args[2:]
    elif args[1] in ("cask"):
        command = ["brew", "cask"] + args[2:]
    elif args[1] in ("python", "py", "pip"):
        command = ["pip"] + args[2:]
    elif args[1] in ("ruby", "rb", "gem"):
        command = ["gem"] + args[2:]
    else:
        command = ["brew"] + args[1:]

    command_process = subprocess.call(command)
