# -*- coding: utf-8 -*-
word = "stressed"
new_word = ""
for i in reversed(range(len(word))):
    new_word = new_word + word[i]
print new_word

print word[::-1]