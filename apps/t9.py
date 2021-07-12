import gzip
import itertools

class T9Decoder:
    """ Работаем с шифром T9
    Методы:
        getT9RussianMatch(str)
    """
    def __init__(self):

        with gzip.open('static/russian.txt.gz', 'r') as f:
            self.russian_words = set(f.read().decode('cp1251').lower().split())

        with open('static/english_alpha.txt') as word_file:
            self.english_words = set(word_file.read().lower().split())

        self.t9_dict_ru = {
            '2':('а','б','в','г'),
            '3':('д','е','ж','з'),
            '4':('и','й','к','л'),
            '5':('м','н','о','п'),
            '6':('р','с','т','у'),
            '7':('ф','х','ц','ч'),
            '8':('ш','щ','ъ','ы'),
            '9':('ь','э','ю','я'),
        }

        self.t9_dict_en = {
            '2':('a','b','c'),
            '3':('d','e','f'),
            '4':('g','h','i'),
            '5':('j','k','l'),
            '6':('m','n','o'),
            '7':('p','q','r','s'),
            '8':('t','u','v'),
            '9':('w','x','y','z'),
        }

        assert 'островский' in self.getT9RussianMatch('5 6 6 6 5 2 6 4 4 4')

    def getT9RussianMatch(self, inputStr):
        outputStr = ''
        inputStr = inputStr.lower()
        testlist = []

        if len(set(inputStr).intersection('23456789')) == 0:
            return 'Ошибка входных данных. Принимаются цифры 2 3 4 5 6 7 8 9.'

        for letter in inputStr:
            if letter in '23456789':
                testlist.append(self.t9_dict_ru.get(letter,''))

        for letters_combo in list(itertools.product(*testlist)):
            new_word = ''.join(letters_combo)
            if new_word in self.russian_words:
                if outputStr != '':
                    outputStr += ', '
                outputStr += new_word

        return outputStr

    def getT9EnglishMatch(self, inputStr):
        outputStr = ''
        inputStr = inputStr.lower()
        testlist = []

        for letter in inputStr:
            if letter in '23456789':
                testlist.append(self.t9_dict_en.get(letter,''))

        for letters_combo in list(itertools.product(*testlist)):
            new_word = ''.join(letters_combo)
            if new_word in self.english_words:
                if outputStr != '':
                    outputStr += ', '
                outputStr += new_word

        return outputStr

    def getT9numbers(self, inputStr):
        outputStr = ''
        inputStr = inputStr.lower()
        # Делаю словарь наоборот - буквы в цифры
        t9_reverse = {
            'ё':'3',
        }
        # Russian
        for k,v in self.t9_dict_ru.items():
            for letter in v:
                t9_reverse[letter] = k
        # English
        for k,v in self.t9_dict_en.items():
            for letter in v:
                t9_reverse[letter] = k

        for letter in inputStr:
            outputStr += t9_reverse.get(letter,'')

        return outputStr

if __name__ == '__main__':

    t9 = T9Decoder()
    print(t9.getT9RussianMatch('5 6 6 6 5 2 6 4 4 4'))
    print(t9.getT9RussianMatch('8 3 2 7 3 5 4 5'))
    print(t9.getT9RussianMatch('4 5 5 3 5 5'))
    print(t9.getT9RussianMatch('привет'))
    print(t9.getT9RussianMatch('455355'))
    print(t9.getT9RussianMatch('1564236'))

    print(t9.getT9EnglishMatch('43556'))
    print(t9.getT9EnglishMatch('4 3 5 5  6'))

    print(t9.getT9numbers('привет'))
    print(t9.getT9numbers('Hello'))