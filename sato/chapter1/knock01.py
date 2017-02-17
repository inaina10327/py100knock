# -*- coding: utf-8 -*-
word = u"パタトクカシーー"
new_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        new_word += word[i]
print new_word

print word[::2]