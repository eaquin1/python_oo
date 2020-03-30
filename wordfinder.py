"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Returns a random word from a input file
    
    >>> wf = WordFinder("animals.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'squirrel']
    True

    >>> wf.random() in ['cat', 'dog', 'squirrel']
    True

    >>> wf.random() in ['cat', 'dog', 'squirrel']
    True
    """
    def __init__(self, path):
        """Read the dictionary and reports # items read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """WordFinder that excludes blank lines and comments
    >>> sw = SpecialWordFinder("hash_tags.txt")
    3 words read

    >>> sw.random() in ['apple', 'plum', 'grape']
    True

    >>> sw.random() in ['apple', 'plum', 'grape']
    True

    >>> sw.random() in ['apple', 'plum', 'grape']
    True
    """
    def parse (self, file):
        return [w.strip() for w in file 
        if w.strip() and not w.startswith("#")]