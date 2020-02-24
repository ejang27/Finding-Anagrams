# Title:
# Name: Eunsoo Jang
# Date: 2/18/2020
# list of n, hashtable is n so space capacity is 2n
# the time: log m for the sorting, n for the linear search in dictionary, so n*log m

import re
import os.path
from os import path
from collections import defaultdict


def main():
    words = ["plekic", "diapers", "teardrop", "nameless", "allergy", "deepak", "impressions", "restrain", "calligraphy", "nepal", "stale", "parliaments", "sucrose","persist", "disintegration"]
    dictionary = open("/usr/share/dict/words").read().split('\n')
    clean_dict = cleanDict(dictionary)
    new_dict =newDictionary(clean_dict)

    for input_word in words:
        print("Anagrams for: ", input_word)
        list = findAnagram(input_word, new_dict)
        for word in list:
            print(word)
        print("\n")

def cleanDict(dictionary):
    clean_dict = []
    cleandictionary = open("cleanDictionary.txt", "w+");
    for word in dictionary:
        if re.search('[^a-zA-Z]', word) is not None:
            continue
        if re.match('[A-Z]', word) is not None:
            continue
        clean_dict.append(word)
    return clean_dict


def newDictionary(clean_dict):
    new_dict = {}
    for word in clean_dict:
        reordered_word = ''.join(sorted(word))
        if reordered_word in new_dict:
            new_dict[reordered_word].append(word)
        else:
            new_dict[reordered_word] = [word]
    return new_dict


def findAnagram(word, dictionary):
    reordered_word = ''.join(sorted(word))
    if reordered_word in dictionary:
        return dictionary.get(reordered_word)



if __name__ == "__main__":
    main()
