# -*- coding: utf-8 -*-
if __name__ == "__main__":
    with open("hightemp.txt", "r")as f:
        s = set([])
        lines = f.readlines()
        for line in lines:
            s.add(line.split()[0])
        print str(s).decode("string-escape")