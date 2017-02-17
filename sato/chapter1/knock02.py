# -*- coding: utf-8 -*-
word1 = u"パトカー"
word2 = u"タクシー"
new_word = ""
for i in range(len(word1)):
    new_word += word1[i] + word2[i]
print new_word