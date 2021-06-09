import json
import time
import gzip
from itertools import combinations

class Anagrams():
    """ Анаграммы по всем словам русского языка
    Методы:
        getOne(str)
        getTwo(str)
    """
    def __init__(self):
        self.start = time.time()
        with gzip.open('static/hash_anagrams_2.json.gz', 'r') as f:
            self.hash_anagrams = json.loads(f.read().decode('cp1251'))

    def getOne(self,inputString):
        '''Get one-word anagram'''
        inputString = inputString.strip()
        inputString = ''.join(sorted(inputString.lower()))
        outputString = self.hash_anagrams.get(inputString,'-')
        # outputString += f'\n - время обработки: {(time.time() - self.start):.3f} с.'
        return outputString

    def getTwo(self,inputString):
        '''Get two-word anagram'''

        def str_diff(str1, str2):
            '''Difference of two strings
            str1 -- longer string
            str2 -- shorter included string
            Return: str1 without str2'''
            string_list = [x for x in str1]
            for y in str2:
                if y in string_list:
                    string_list.remove(y)
            return ''.join(string_list)

        inputString = inputString.strip()
        inputString = ''.join(sorted(inputString.lower()))

        outputString = 'Варианты из двух слов:\n'
        output_words = set()

        for i in range(len(inputString) - 2, int(len(inputString) / 2), -1):
            # iterating from len to half
            for x in combinations(inputString, i):
                y = ''.join(x)
                z = str_diff(inputString, y)  # leftover of letters
                #
                isInAnagrams = (y in self.hash_anagrams
                              and z in self.hash_anagrams)
                # Должно содержать гласные
                hasVowels = True
                if len(z) <= 3 and len(set(z).intersection("аеёиоуыэюя")) == 0:
                    hasVowels = False
                if isInAnagrams and hasVowels:
                    output_words.add(self.hash_anagrams[y] + ' + ' + self.hash_anagrams[z])

        for wordCombo in output_words:
            outputString += wordCombo + '\n'

        # outputString += f'\n - время обработки: {(time.time() - self.start):.3f} с.'

        return outputString

if __name__ == "__main__":

    test = Anagrams()

    print(test.getOne('слово'))
    print(test.getOne('остров'))
    print(test.getOne('оловяный'))

    print(test.getTwo('слово'))
    print(test.getTwo('остров'))
    print(test.getTwo('оловяный'))