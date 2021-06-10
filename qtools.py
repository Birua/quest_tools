"""
    Flask app for quest tools.
    - morse code translator
    - Braille code translator
    - Mendeleev periodic table reference
    - RU/EN alphabet to numbers and reverse
    - RU anagrams (one- and two-word)

    Version History:
      0.09 -- 10/06/21 Braille changes, multiple anagrams
      0.08 -- 09/06/21 cookie size fix, two-word anagrams filter
      0.07 -- 09/06/21 One-word and two-word anagrams
      0.06 -- 07/06/21 Jinja render_template
      0.05 -- 03/06/21 Alphabet
      0.04 -- 02/06/21 Mendeleev Periodic Table
      0.03 -- 02/06/21 Braille conversion
      0.02 -- 01/06/21 Overall design and Morse Code
      0.01 -- 31/05/21 First steps

"""
from flask import Flask, redirect, request, session, render_template
from markupsafe import Markup
from apps.morse import MorseCodeTranslator
from apps.braille import BrailleTranslator
from apps.mendel import PeriodicTable
from apps.anagrams import Anagrams

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'D5r09fAe+!aIB1eRMT4tO*ko(M.w^s'

@app.route('/', methods=['POST', 'GET'])
def qtools():

    if session.get('output_window') is None:
        output_window = ''
        session['output_window'] = ''
    else:
        output_window = session.get('output_window')

    def add_to_output(zapros, otvet):
        # updating Output Window
        if isinstance(zapros, str) and isinstance(otvet, str):
            output_window = session.get('output_window')
            if output_window is None:
                output_window = ''
            output_window = zapros + ' <br> <hr> ' + output_window
            output_window = otvet + ' <br> ' + output_window
            if len(output_window) > 4000:
                output_window = output_window[0:4000]
            session['output_window'] = output_window

    if request.method == 'POST':
        zapros = ''
        otvet = ''
        # print(request.form, request.form.get('braille_txt'))

        # Очистка окна вывода
        if 'clear_submit' in request.form:
            session['output_window'] = ''
            return redirect('/')

        # -- --- .-. ... . -.-. --- -.. . .--. .-. --- -.-. . ... ... .. -. --.
        # Morse Code processing
        # -- --- .-. ... . -.-. --- -.. . .--. .-. --- -.-. . ... ... .. -. --.
        if request.form.get('morse_txt'):
            try:
                zapros = request.form.get('morse_txt')

                morse = MorseCodeTranslator()
                otvet = morse.translate_morse(zapros).replace('\n','<br>')
                # check for empty result - REVERSE: text to morse convert
                if otvet == '<br>':
                    otvet = morse.translate_text(zapros)
                add_to_output(zapros, otvet)
            except:
                zapros = ''
                otvet = 'Error: сбой блока Morse'
                add_to_output(zapros, otvet)
            return redirect('/')

        # ⠠⠞⠗⠁⠝⠎⠇⠁⠞⠊⠝⠛ ⠞⠑⠭⠞ ⠖ ⠠⠛⠗⠁⠙⠑ ⠼⠃ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠊⠎ ⠁ ⠝⠕⠝⠤⠞⠗
        # Braille-Translator
        # ⠠⠞⠗⠁⠝⠎⠇⠁⠞⠊⠝⠛ ⠞⠑⠭⠞ ⠖ ⠠⠛⠗⠁⠙⠑ ⠼⠃ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠊⠎ ⠁ ⠝⠕⠝⠤⠞⠗
        if request.form.get('braille_txt'):
            try:
                zapros = request.form.get('braille_txt')

                braille = BrailleTranslator()
                if zapros.replace(' ','').isnumeric():
                    # цифровые коды Брайля 12 14 и т.п.
                    otvet = braille.convert_codes(zapros).replace('\n','<br>')
                    otvet += '<br> <braille>' + braille.translate_text(otvet.split('<br>')[1]) + '</braille>'
                else:
                    if max([ord(_) for _ in zapros]) > 10_000:
                        # Это коды Брайля UTF-8, которые конвертируем в обычный текст
                        otvet = braille.convertBrailleUnicodes(zapros)
                    else:
                        # Это обычный текст, который конвертируем в коды Брайля
                        otvet = '<braille>' + braille.translate_text(zapros) + '</braille>'

                add_to_output(zapros, otvet)
            except:
                zapros = ''
                otvet = 'Error: сбой блока Braille'
                add_to_output(zapros, otvet)
            return redirect('/')

        # H	He	Li	Be	B	C	N	O	F	Ne	Na	Mg	Al	Si	P	S	Cl	Ar
        # Periodic Table Mendeleev
        # H	He	Li	Be	B	C	N	O	F	Ne	Na	Mg	Al	Si	P	S	Cl	Ar
        if request.form.get('mendel_txt'):
            try:
                zapros = request.form.get('mendel_txt')

                mendel = PeriodicTable()
                otvet = ''
                if len(zapros.split()) == 1:
                    # Короткий запрос на 1 элемент
                    if zapros.isnumeric():
                        # Атомный номер элемента
                        if len(mendel.elementByNumber(zapros)[1]) > 1:
                            otvet = ' '.join([str(_) for _ in mendel.elementByNumber(zapros)])
                        else:
                            otvet = mendel.elementByNumber(zapros)
                    else:
                        # Поиск по русскому имени
                        otvet = ' '.join([str(_) for _ in mendel.elementByNameRu(zapros)])
                        if otvet.strip() == '':
                            # по символу элемента - Ti Na Sb etc.
                            otvet += ' '.join([str(_) for _ in mendel.elementBySymbol(zapros)])
                else:
                    # Групповой запрос на несколько элементов
                    if zapros.replace(' ','').isnumeric():
                        # по атомному номеру
                        for number in zapros.split():
                            otvet += str(mendel.elementByNumber(number)[3]) + ' '
                    else:
                        #
                        # по русскому имени выдаем Символ элемента
                        for element_name in zapros.split():
                            otvet += str(mendel.elementByNameRu(element_name)[3]) + ' '
                        if otvet.strip() == '':
                            # по символам элемента (Ti Na Sb etc.) выдаем АтомныйНомер Хим. Элемента
                            for element_name in zapros.split():
                                otvet += str(mendel.elementBySymbol(element_name)[0]) + ' '
                add_to_output(zapros, otvet)
            except:
                zapros = ''
                otvet = 'Error: сбой блока Mendeleev'
                add_to_output(zapros, otvet)
            return redirect('/')

        # ----------абвгдеёжзийклмнопрстуфхцчшщъыьэюя----------
        # Алфавит
        # ----------абвгдеёжзийклмнопрстуфхцчшщъыьэюя----------
        if request.form.get('alpha_txt'):
            try:
                zapros = request.form.get('alpha_txt')
                otvet = ''
                alphabet_en = '0abcdefghijklmnopqrstuvwxyz'
                alphabet_ru = '0абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

                if zapros.replace(' ', '').isnumeric():
                    otvet_ru = ''
                    otvet_en = ''
                    for letter_number in zapros.split():
                        letter_number = int(letter_number)
                        otvet_ru += alphabet_ru[letter_number] if letter_number < len(alphabet_ru) else ''
                        otvet_en += alphabet_en[letter_number] if letter_number < len(alphabet_en) else ''
                    otvet = otvet_ru + '<br>' + otvet_en
                else:
                    for letter in zapros.lower():
                        letter_number = ''
                        # выдавать номер только для букв, которые есть в alphabet_ru
                        letter_number = str(alphabet_ru.index(letter)) if letter in alphabet_ru else ''
                        if letter_number == '':
                            # буквы не было в русском, ищем в английском
                            letter_number = str(alphabet_en.index(letter)) if letter in alphabet_en else ''
                        otvet += letter_number + ' '
                add_to_output(zapros, otvet)
            except:
                zapros = ''
                otvet = 'Error: сбой блока Alpha'
                add_to_output(zapros, otvet)
            return redirect('/')

        # ----------Анаграммы-ыммарганА----------
        # Анаграммы
        # ----------Анаграммы-ыммарганА----------
        if request.form.get('anagrams_txt'):

            try:
                zapros = request.form.get('anagrams_txt')
                if len(zapros.split()) == 1:
                    # Одно слово
                    otvet = f'Букв: {len(zapros.strip())}<br>'
                    otvet += 'Полная анаграмма: '
                    anagram = Anagrams()
                    otvet += anagram.getOne(zapros).replace('\n','<br>')
                    otvet += '<br>' + anagram.getTwo(zapros).replace('\n', '<br>')
                else:
                    # Несколько слов:
                    otvet = ''
                    anagram = Anagrams()
                    for word in zapros.split():
                        otvet += f'{word.strip()} ({len(word.strip())}): '
                        otvet += f'{anagram.getOne(word)}<br>'

                add_to_output(zapros, otvet)
            except:
                zapros = ''
                otvet = 'Error: сбой блока Anagrams'
                add_to_output(zapros, otvet)
            return redirect('/')

    return render_template('quest_tools.html', output_window=Markup(session['output_window']), current_version='0.09')

if __name__ == '__main__':

    app.run(debug=True)