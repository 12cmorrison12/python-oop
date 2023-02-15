"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Class for finding random words from a dictionary"""

    def __init__(self, path):
        """Reads dictionary and gives back number of items"""

        file = open(path)
        self.words = self.parse(file)

        return f"{len(self.words)} words listed."

    def parse(self, file):
        """Parses provided file/list into a list of words"""

        return [word.stip() for word in file]

    def random_word(self):
        """Returns a random word"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized word finder that gets rid of blank lines and comments"""

    def parse(self, file):
        """Parses provided file into a list of words, skipping over blank lines and comment blocks"""

        return [word.strip() for word in file if word.strip() and not word.startswith('#')]