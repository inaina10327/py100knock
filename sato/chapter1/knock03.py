# -*- coding: utf-8 -*-
sentence = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
words = sentence.split()
words_cnt = []
for word in words:
    words_cnt.append(len(word))
print words_cnt

words_cnt = [len(w) for w in words]
print words_cnt