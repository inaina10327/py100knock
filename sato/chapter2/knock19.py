# -*- coding: utf-8 -*-
from collections import Counter
if __name__ == "__main__":
    with open("hightemp.txt", "r")as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.split()
            words.append(line[0])
        counter = Counter(words)
        for (word, cnt) in counter.most_common():
            print str(word).decode("string-escape"), cnt

# sato2@sato2-VirtualBox:~/py100knock1/sato/chapter2$ cut -f1 hightemp.txt | sort | uniq -c
#       2 愛知県
#       1 愛媛県
#       2 岐阜県
#       3 群馬県
#       1 高知県
#       3 埼玉県
#       3 山形県
#       3 山梨県
#       2 静岡県
#       2 千葉県
#       1 大阪府
#       1 和歌山県
