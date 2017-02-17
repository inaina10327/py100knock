# -*- coding: utf-8 -*-
import random
def typoglycemia(word_list):
    new_word = ""
    new_str = ""
    for word in word_list:
        if len(word) > 4:
            new_word += word[0]
            random_word = list(word[1:len(word) - 1])
            random.shuffle(random_word)
            random_word = "".join(random_word)
            new_word += random_word
            new_word += word[len(word) - 1]
            new_str += new_word + " "
            new_word = ""
        else:
            new_str += word + " "
    return new_str



if __name__ == "__main__":
    string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print string.rsplit()
    print typoglycemia(string.rsplit())