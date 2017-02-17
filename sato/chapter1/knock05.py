# -*- coding: utf-8 -*-
def n_gram(str, n):
    grams = []
    for i in range(len(str) - (n - 1)):
        grams.append(str[i:i+n])
    return grams

if __name__ == "__main__":
    string = "I am an NLPer"
    print "単語bi-gram"
    print n_gram(string.split(), 2)
    print "文字bi-gram"
    print n_gram(string.replace(" ", ""), 2)
    print "単語tri-gram"
    print n_gram(string.split(), 3)