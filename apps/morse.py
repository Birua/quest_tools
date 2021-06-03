class MorseCodeTranslator:
    ''' To Morse Code and from Morse Code
    RU and EN
    Methods:
        translate_morse(str) - Morse to EN and RU
        translate_text(str) - EN or RU to Morse Code
    '''
    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
    morse_ru = {
        'а': '.-',
        'б': '-...',
        'в': '.--',
        'г': '--.',
        'д': '-..',
        'е': '.',
        'ё': '.',
        'ж': '...-',
        'з': '--..',
        'и': '..',
        'й': '.---',
        'к': '-.-',
        'л': '.-..',
        'м': '--',
        'н': '-.',
        'о': '---',
        'п': '.--.',
        'р': '.-.',
        'с': '...',
        'т': '-',
        'у': '..-',
        'ф': '..-.',
        'х': '....',
        'ц': '-.-.',
        'ч': '---.',
        'ш': '----',
        'щ': '--.-',
        'ъ': '.--.-.',
        'ы': '-.--',
        'ь': '-..-',
        'э': '..-..',
        'ю': '..--',
        'я': '.-.-',
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }

    def translate_morse(self, morse, strict=True):

        """
        Translates morse code to text using a small set of Internation Morse code.

        Accepts:
            morse (str): A string of morse code to translate
            strict (bool): If True, parse and return morse code containing 4 spaces

        Returns:
            str: A translated string of text
        """

        if morse == "":
            return "You must provide a string of text to translate"

        if "    " in morse:
            if strict:
                return "Unable to translate morse code. Found 4 spaces in morse code string"
            else:
                morse.replace("    ", "   ")

        translation = ""
        translation_ru = ""

        words = morse.split("   ")

        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                for k, v in self.morse.items():
                    if char == v:
                        translation += k
                        break
                for k, v in self.morse_ru.items():
                    if char == v:
                        translation_ru += k
                        break
            translation += " "
            translation_ru += " "

        return translation.rstrip() + '\n' + translation_ru.rstrip()

    def translate_text(self, text):

        """
        Translates text to morse code using a small set of Internation Morse code.

        Accepts:
            text (str): A string of text to translate

        Returns:
            str: A string translated to Morse code
        """

        if text == "":
            return "(Морзе) Введите текст."

        translation = ""

        words = text.split(" ")

        for word in words:
            w = list()
            for char in word:
                if char.lower() in self.morse:
                    w.append(self.morse[char.lower()])
                elif char.lower() in self.morse_ru:
                    w.append(self.morse_ru[char.lower()])

            translation += " ".join(w)
            translation += "   "

        return translation.rstrip()


if __name__ == '__main__':
     translator = MorseCodeTranslator()

     # text = "This string has been translated to morse code and back again"
     text = "Тхис стринг хас беен транслатед то морсе цоде анд бацк агаин"
     # text = "Тест 1 раз 2 два 3 три!"

     # Translate text to morse code
     morse = translator.translate_text(text)
     # morse = "- . ... - .---- "

     # Translate morse code to text
     translated_text = translator.translate_morse(morse)

     print(morse)
     print(translated_text)

     # print(ord(translator.translate_morse('aaa')))
