# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("hightemp.txt", "r")as f:
        cnt = 0
        for line in f:
            cnt += 1
        print cnt

#/usr/bin/python2.7 /home/sato2/py100knock1/sato/chapter2/knock10.py
#24


# sato2@sato2-VirtualBox:~/py100knock1/sato/chapter2$ wc hightemp.txt
#  24  96 813 hightemp.txt
