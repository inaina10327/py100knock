# -*- coding: utf-8 -*-
sentence = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element_symbol = {}
words = sentence.split()
for i in range(len(words)):
    if i + 1 in num:
        element_symbol[words[i][:1]] = i + 1
        print words[i][:1]
    else:
        element_symbol[words[i][:2]] = i + 1
        print words[i][:2]
print element_symbol