import re
from typing import Dict



class WordConverter:
    def __init__(self):
        self.dictionary = self.read_dict_file()

    def read_dict_file(self) -> Dict:
        path = "./data/dict"
        res = {}
        with open(path, encoding="utf-8") as f:
            for words in [(line.strip()).split(" ") for line in f.readlines()]:
                if len(words) >= 2:
                    res[words[0]] = words[1]
        return res
        
    def get_dict(self):
        return self.dictionary

    def convert(self, word):
        return self.dictionary.get(word, word)

    def trim_space(self, line):
        return re.sub("\s+", " ", line)

    def word_split(self, line):
        return self.trim_space(line).split(" ")

