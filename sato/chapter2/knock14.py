# -*- coding: utf-8 -*-
import sys
if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        with open("hightemp.txt", "r")as f:
            cnt = 1
            for line in f:
                if cnt > int(args[1]):
                    break
                else:
                    print line
                cnt += 1
    else:
        print "error"