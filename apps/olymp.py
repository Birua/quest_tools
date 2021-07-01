import pandas as pd
import time

class OlympSolver():
    """ Помощник для олимпиеек по sociation.org
        одно слово -- список ассоциаций
        два слова -- пересечение ассоциаций
    Методы:
        getSociationsForOne(str)
        getSociationsForTwo(str)
    """
    def __init__(self):
        self.kubrai = pd.read_csv('static/Kubrai.csv', header=None, sep='\t')
        self.sociation = pd.read_csv("static/sociation_2.csv", header=None)

        assert 'море' in self.getSociationsForOne('пляж')
        assert 'море' in self.getSociationsForTwo('пляж песок')

    def getSociationsForOne(self,inputString):
        # для одного слова
        if not isinstance(inputString,str):
            return 'One word as str required.'

        word1 = inputString.lower()

        wordlist1 = set(self.sociation[self.sociation[0] == word1][1]) \
                    | set(self.sociation[self.sociation[1] == word1][0]) \
                    | set(self.kubrai[self.kubrai[0] == word1][1]) \
                    | set(self.kubrai[self.kubrai[1] == word1][0])

        outputString = ''
        for word in wordlist1:
            outputString += word + ', '

        return outputString

    def getSociationsForTwo(self,inputString):
        # для двух слов
        if not isinstance(inputString,str):
            return 'Two words as str required.'

        word1 = inputString.split()[0]
        word2 = inputString.split()[1]
        word1 = word1.lower()
        word2 = word2.lower()

        wordlist1 = set(self.sociation[self.sociation[0] == word1][1]) \
                    | set(self.sociation[self.sociation[1] == word1][0]) \
                    | set(self.kubrai[self.kubrai[0] == word1][1]) \
                    | set(self.kubrai[self.kubrai[1] == word1][0])
        wordlist2 = set(self.sociation[self.sociation[0] == word2][1]) \
                    | set(self.sociation[self.sociation[1] == word2][0]) \
                    | set(self.kubrai[self.kubrai[0] == word2][1]) \
                    | set(self.kubrai[self.kubrai[1] == word2][0])

        wordlist = wordlist1 & wordlist2

        outputString = ''
        for word in wordlist:
            outputString += word + ', '

        return outputString

if __name__ == '__main__':

    a = OlympSolver()

    print(a.getSociationsForOne('пляж'))
    print(a.getSociationsForTwo('пляж песок'))
    print(a.getSociationsForOne(1))
    print(a.getSociationsForTwo(1.56))