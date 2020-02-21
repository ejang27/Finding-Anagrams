#Title: cleanDictionary.py
#Name: Eunsoo Jang
#Date: 2/18/2020

import re
import os.path
from os import path


def main():
    input_file = open("cleanDictionary.txt", "w+")
    newDictionary(input_file)

def newDictionary(dictionary):
    newDict = dict()
    for word in dictionary:
        reordered_word = word.sort()
        if(reordered_word in newDict):
            newDict[reordered_word] = word
        else:
            newDict[reordered_word] = word

def findAnagram(word, dictionary):
    reordered_word = word.sort()
    if(reordered_word in dictionary):
        return dictionary[reordered_word]
