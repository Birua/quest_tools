class BrailleTranslator:
    ''' Braille translator
    Methods:
        translate_text(str) - to Braille utf-8
        translate_codes(str) - from 6-slot coding to Braille
        translate_braille(str) - from Braille utf to Latin
    '''
    characterUnicodes = {'a': '\u2801', 'b': '\u2803', 'k': '\u2805', 'l': '\u2807', 'c': '\u2809', 'i': '\u280A',
                         'f': '\u280B', 'm': '\u280D', 's': '\u280E', 'p': '\u280F', 'e': '\u2811', 'h': '\u2813',
                         'o': '\u2815', 'r': '\u2817',
                         'd': '\u2819', 'j': '\u281A', 'g': '\u281B', 'n': '\u281D', 't': '\u281E', 'q': '\u281F',
                         'u': '\u2825', 'v': '\u2827',
                         'x': '\u282D', 'z': '\u2835', 'w': '\u283A', 'y': '\u283D', 'num': '\u283C', 'caps': '\u2820',
                         '.': '\u2832',
                         "'": '\u2804', ',': '\u2802', '-': '\u2824', '/': '\u280C', '!': '\u2816', '?': '\u2826',
                         '$': '\u2832', ':': '\u2812',
                         ';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': ' ',
                         '1': '\u2801', '2': '\u2803', '3': '\u2809', '4': '\u2819', '5': '\u2811',
                         '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A',
                         'а': '\u2801',
                         'б': '\u2803',
                         'в': '\u283A',
                         'г': '\u281B',
                         'д': '\u2819',
                         'е': '\u2811',
                         'ё': '\u2821',
                         'ж': '\u281A',
                         'з': '\u2835',
                         'и': '\u280A',
                         'й': '\u282F',
                         'к': '\u2805',
                         'л': '\u2807',
                         'м': '\u280D',
                         'н': '\u281D',
                         'о': '\u2815',
                         'п': '\u280F',
                         'р': '\u2817',
                         'с': '\u280E',
                         'т': '\u281E',
                         'у': '\u2825',
                         'ф': '\u280B',
                         'х': '\u2813',
                         'ц': '\u2809',
                         'ч': '\u281F',
                         'ш': '\u2831',
                         'щ': '\u282D',
                         'ъ': '\u2837',
                         'ы': '\u282E',
                         'ь': '\u283E',
                         'э': '\u282A',
                         'ю': '\u2833',
                         'я': '\u282B',
                         }

    brailleDots = {
        'a': 1,
        'b': 12,
        'c': 14,
        'd': 145,
        'e': 15,
        'f': 124,
        'g': 1245,
        'h': 125,
        'i': 24,
        'j': 245,
        'k': 13,
        'l': 123,
        'm': 134,
        'n': 1345,
        'o': 135,
        'p': 1234,
        'q': 12345,
        'r': 1235,
        's': 234,
        't': 2345,
        'u': 136,
        'v': 1236,
        'w': 2456,
        'x': 1346,
        'y': 13456,
        'z': 1356,
        '1': 1,
        '2': 12,
        '3': 14,
        '4': 145,
        '5': 15,
        '6': 124,
        '7': 1245,
        '8': 125,
        '9': 24,
        '0': 245,
        ',': 2,
        ';': 23,
        ':': 25,
        '.': 256,
        '?': 236,
        '!': 235,
        '‘': 3,
    }
    brailleCodes = {
        1: 'a',
        12: 'b',
        14: 'c',
        145: 'd',
        15: 'e',
        124: 'f',
        1245: 'g',
        125: 'h',
        24: 'i',
        245: 'j',
        13: 'k',
        123: 'l',
        134: 'm',
        1345: 'n',
        135: 'o',
        1234: 'p',
        12345: 'q',
        1235: 'r',
        234: 's',
        2345: 't',
        136: 'u',
        1236: 'v',
        2456: 'w',
        1346: 'x',
        13456: 'y',
        1356: 'z',
        235: '!',
        2: ',',
        256: '.',
        25: ':',
        23: ';',
        236: '?',
        3: '‘',
    }
    brailleCodes_full = {
    "0": ["&nbsp;", "&nbsp;", "&nbsp;", "&nbsp;"],
    "1": ["a", "а", "1", "&#x2801;"],
   "12": ["b", "б", "2", "&#x2803;"],
   "14": ["c", "ц", "3", "&#x2809;"],
  "145": ["d", "д", "4", "&#x2819;"],
   "15": ["e", "е", "5", "&#x2811;"],
  "124": ["f", "ф", "6", "&#x280B;"],
 "1245": ["g", "г", "7", "&#x281B;"],
  "125": ["h", "х", "8", "&#x2813;"],
   "24": ["i", "и", "9", "&#x280A;"],
  "245": ["j", "ж", "0", "&#x281A;"],
   "13": ["k", "к", "", "&#x2805;"],
  "123": ["l", "л", "", "&#x2807;"],
  "134": ["m", "м", "", "&#x280D;"],
 "1345": ["n", "н", "", "&#x281D;"],
  "135": ["o", "о", "", "&#x2815;"],
 "1234": ["p", "п", "", "&#x280F;"],
"12345": ["q", "ч", "", "&#x281F;"],
 "1235": ["r", "р", "", "&#x2817;"],
  "234": ["s", "с", "", "&#x280E;"],
 "2345": ["t", "т", "", "&#x281E;"],
  "136": ["u", "у", "", "&#x2825;"],
 "1236": ["v", "v", "", "&#x2827;"],
 "2456": ["w", "в", "", "&#x283A;"],
 "1346": ["x", "щ", "", "&#x282D;"],
"13456": ["y", "y", "", "&#x283D;"],
 "1356": ["z", "з", "", "&#x2835;"],
   "16": ["ё", "ё", "", "&#x2821;"],
"12346": ["й", "й", "", "&#x282F;"],
  "156": ["ш", "ш", "", "&#x2831;"],
"12356": ["ъ", "ъ", "", "&#x2837;"],
 "2346": ["ы", "ы", "", "&#x282E;"],
"23456": ["ь", "ь", "", "&#x283E;"],
  "246": ["э", "э", "", "&#x282A;"],
 "1256": ["ю", "ю", "", "&#x2833;"],
 "1246": ["я", "я", "", "&#x282B;"],
  "236": ["«", "«", "", "&#x2826;"],
  "356": ["»", "»", "", "&#x2834;"],
   "36": ["&mdash;", "", "&nbsp;", "&#x2824;"],
  "256": [".", ".", ".", "&#x2832;"],
    "2": [",", ",", ",", "&#x2802;"],
   "26": ["?", "?", "", "&#x2822;"],
   "23": [";", ";", "", "&nbsp;"],
  "235": ["!", "!", "", "&#x2816;"],
 "3456": ["&rarr;", "&rarr;", "&rarr;", "&#x283C;"],
    "6": ["&uarr;", "&uarr;", "", "&nbsp;"],
}
    numberPunctuations = ['.', ',', '-', '/', '$']
    escapeCharacters = ['\n', '\r', '\t']

    def convert_codes(self, codesToConvert):
        convertedText = ''
        convertedText_ru = ''
        for code_str in codesToConvert.split():
            if code_str.isnumeric():
                code_str = ''.join(sorted(code_str))
                convertedText += self.brailleCodes_full.get(code_str, ['_',''])[0]
                convertedText_ru += self.brailleCodes_full.get(code_str, ['','_'])[1]
        return convertedText + '\n' + convertedText_ru

    def translate_text(self, textToConvert):
        if type(textToConvert) is not str:
            raise TypeError("Only strings can be converted")
        return self.convert(textToConvert)

    def convert(self, textToConvert):
        isNumber = False
        convertedText = ''
        for character in textToConvert:
            if character in self.escapeCharacters:
                convertedText += character
                continue
            if character.isupper():
                convertedText += self.characterUnicodes.get('caps')
                character = character.lower()
            if character.isdigit():
                if not isNumber:
                    isNumber = True
                    convertedText += self.characterUnicodes.get('num')
            else:
                if isNumber and character not in self.numberPunctuations:
                    isNumber = False
            convertedText += self.characterUnicodes.get(character,'')
        return convertedText

    def convertBrailleUnicodes(self,textToConvert):
        # remapping the Unicodes dictionary
        unicodeCharacters = {v: k for k, v in self.characterUnicodes.items()}
        convertedText = ''
        for character in textToConvert:
            convertedText += unicodeCharacters[character]
        return convertedText


if __name__ == '__main__':
     braille = BrailleTranslator()
     
     print(braille.translate_text('s_s'))
     print(braille.convert_codes('23456'))

     print(braille.convertBrailleUnicodes(braille.translate_text('easy game')))


