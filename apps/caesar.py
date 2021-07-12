import time
import gzip


class CaesarDecoder:
    """ Работаем с шифром Цезаря
    Методы:
        getRussianMatch(str)
        getEnglishMatch(str)
        getAllEnglish(str)
        getAllRussian(str)
    """

    def __init__(self):
        self.alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

        assert 'Чу, я слышу пушек гром!' in self.getAllRussian('Ёв, н аъйжв ювжущ сяэы!')
        assert 'This is some string! Great!' in self.getAllEnglish('Iwxh xh hdbt higxcv! Vgtpi!')
        # assert 'Чу, я слышу пушек гром!' in self.getRussianMatch('Ёв, н аъйжв ювжущ сяэы!')
        # assert 'This is some string! Great!' in self.getEnglishMatch('Iwxh xh hdbt higxcv! Vgtpi!')
        
    def _getAll(self, inputStr, alphabet):
        outputStr = '00: '
        # going through all shifts
        for i in range(len(alphabet)):
            for word in inputStr.split():
                for letterOriginal in word:
                    # remember letter CASE
                    letter = letterOriginal.lower()
                    if letter in alphabet:
                        letter_shift = i + alphabet.find(letter)
                        # circling shift
                        if letter_shift >= len(alphabet):
                            letter_shift = letter_shift - len(alphabet)
                        # Check for CASE
                        if letter != letterOriginal:
                            outputStr += alphabet[letter_shift].upper()
                        else:
                            outputStr += alphabet[letter_shift]
                    else:
                        outputStr += letterOriginal
                outputStr += ' '

            if i < len(alphabet) - 1:
                outputStr += f'\n{i + 1:02d}: '

        return outputStr
        
    def getAllRussian(self, inputStr):
        return self._getAll(inputStr, self.alphabet_ru)

    def getAllEnglish(self, inputStr):
        return self._getAll(inputStr, self.alphabet_en)

    def getRussianMatch(self, inputStr):

        with gzip.open('static/russian.txt.gz', 'r') as f:
            russian_words = set(f.read().decode('cp1251').lower().split())

        all_variants = self._getAll(inputStr, self.alphabet_ru)
        outputStr = ''
        for variant in all_variants.split('\n'):
            count_match = 0
            # [4:] is skipping leading shift number e.g. '18: '
            for word in variant[4:].split():
                # leave only lower case letters
                word = ''.join([_ for _ in word.lower() if _ in self.alphabet_ru])
                # check word in dictionary
                if len(word) > 2 and word in russian_words:
                    count_match += 1

            if count_match >= len(variant[4:].split()) / 2:
                outputStr += variant + '\n'

        return outputStr

    def getEnglishMatch(self, inputStr):

        with open('static/english_alpha.txt') as word_file:
            english_words = set(word_file.read().lower().split())

        all_variants = self._getAll(inputStr, self.alphabet_en)
        outputStr = ''
        for variant in all_variants.split('\n'):
            count_match = 0
            # [4:] is skipping leading shift number e.g. '18: '
            for word in variant[4:].split():
                # leave only lower case letters
                word = ''.join([_ for _ in word.lower() if _ in self.alphabet_en])
                # check word in dictionary
                if len(word) > 2 and word in english_words:
                    count_match += 1
            if count_match >= len(variant[4:].split())/2:
                outputStr += variant + '\n'

        return outputStr

if __name__ == '__main__':
    start = time.time()
    caesar = CaesarDecoder()
    # print(caesar.getAllRussian('Ёв, н аъйжв ювжущ сяэы!'))
    # print(caesar.getAllEnglish('Iwxh xh hdbt higxcv! Vgtpi!'))
    # print(caesar.getAllRussian('Проверка!'))
    print(caesar.getRussianMatch('Ёв, н аъйжв ювжущ сяэы!'))
    print(caesar.getRussianMatch('Мнлявнзэ!'))
    print(caesar.getEnglishMatch('Iwxh xh hdbt higxcv! Vgtpi!'))
    print(f'All took: {(time.time() - start):.3f} s')