# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("hightemp.txt", "r")as open_f:
        with open("col1.txt", "w")as col1:
            with open("col2.txt", "w")as col2:
                for line in open_f:
                    line = line.rsplit()
                    col1.write(line[0] + "\n")
                    col2.write(line[1] + "\n")