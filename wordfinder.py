"""Word Finder: finds random words from a dictionary."""
import random
word_list = []

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
    def __init__(self, file):
        self.file = file
        self.parse_file(file)
        self.word_list_length()

    def parse_file(self):
        with open(self.file, 'r') as file:
            for line in file:
                line = line.strip()
                word_list.append(line)
        
    
    def word_list_length(self):
        print(f"{len(word_list)} words read")

    def random(self):
        return random.choice(word_list)

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
    def parse_file(self, file):
        return [w.strip() for w in file if w.strip() and not w.startswith("#")]