# -*- coding: utf-8 -*-
import sys
if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        line_num = int(args[1])
        with open("hightemp.txt", "r")as f:
            lines = f.readlines()
            width = len(lines) / line_num
            cnt = 0
            for line in lines:
                if cnt % width == 0 and cnt != 0:
                    print "--------------"
                print line
                cnt += 1
    else:
        print "error"