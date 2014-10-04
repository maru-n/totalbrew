#!/usr/bin/python
# encoding: UTF-8

import sys
import subprocess

if __name__ == '__main__':
    args = sys.argv
    print args

    if len(args)==1:
        print "usage: totalbrew brew"
        sys.exit()

    command = "brew"
    command_args = args[2:] if args[1]=="brew" else args[1:]
    command_list = [command] + command_args
    command_process = subprocess.Popen(command_list)
