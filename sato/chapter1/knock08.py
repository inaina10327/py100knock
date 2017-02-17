# -*- coding: utf-8 -*-
def cipher(str):
    enigma = ""
    for i in range(len(str)):
        if str[i].islower():
            enigma += chr(219 - ord(str[i]))
        else:
            enigma += str[i]
    return enigma
if __name__ == "__main__":

    print cipher("paraparaparadiseAAA123")