# -*- coding: utf-8 -*-
def n_gram(str, n):
    grams = []
    for i in range(len(str) - (n - 1)):
        grams.append(str[i:i+n])
    return grams

if __name__ == "__main__":
    word1 = "paraparaparadise"
    word2 = "paragraph"
    word1_bi_gram = n_gram(word1.replace(" ", ""), 2)
    word2_bi_gram = n_gram(word2.replace(" ", ""), 2)
    X = set(word1_bi_gram)
    Y = set(word2_bi_gram)
    print "X or Y"
    print X.union(Y)
    print "X and Y"
    print X.intersection(Y)
    print "X - Y"
    print X.difference(Y)
    print "Y - X"
    print Y.difference(X)
    print "'se' in X"
    print 'se' in X
    print "'se' in Y"
    print 'se' in Y