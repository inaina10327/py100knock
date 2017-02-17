# -*- coding: utf-8 -*-
import sys
if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        line_num = int(args[1])
        with open("hightemp.txt", "r")as f:
            lines = f.readlines()[-line_num:]
            for line in lines:
                print line
    else:
        print "error"