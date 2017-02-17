# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("marge13.txt", "w")as w_f:
        with open("col1.txt", "r")as col1:
            with open("col2.txt", "r")as col2:
                for (col1_line, col2_line) in zip(col1, col2):
                    w_f.write(col1_line.replace("\n", "") + "\t" + col2_line)