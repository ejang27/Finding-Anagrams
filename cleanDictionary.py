

#Title: cleanDictionary.py
#Name: Eunsoo Jang
#Date: 2/18/2020

import re
import os.path
from os import path


def main():

    output_file = open("cleanDictionary.txt", "w+")
    input_file = open("/usr/share/dict/words").read().split('\n')

    newDictionary = []


if __name__ == "__main__":
    main()
