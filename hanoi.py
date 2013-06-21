#!/usr/bin/python

import os, sys

def hanoi2(h, source, dest, temp):
    if 1 == h:
        print "Moving %i from %s to %s" % (h, source, dest)
        return

    else:
        hanoi2(h-1, source, temp, dest)
        print "Moving %i from %s to %s" % (h, source, dest)
        hanoi2(h-1, temp, dest, source)


def hanoi(num_disks):
    if 0 == num_disks:
        print "Not allowed to specify 0 disks"
        sys.exit(-1)

    if num_disks < 0:
        print "Number of disks must be positive"
        sys.exit(-1)


    hanoi2(num_disks, "A", "C", "B")


def main():

    if 1 == len(sys.argv):
        print "You must specify the number of disks to move in the command line"
        sys.exit(-1)

    try:
        num_disks = int(sys.argv[1])
    except:
        print "Could not cast '%s' to an integer" % sys.argv[1]
        sys.exit(-1)

    hanoi(num_disks)


if __name__ == "__main__":
    main()