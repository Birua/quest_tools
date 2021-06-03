"""
    Flask app for quest tools.
    - morse code translator

    Version History:
      0.05 -- 03/06/21 Aphabet
      0.04 -- 02/06/21 Mendeleev Periodic Table
      0.03 -- 02/06/21 Braille conversion
      0.02 -- 01/06/21 Overall design and Morse Code
      0.01 -- 31/05/21 First steps

"""
from flask import Flask, redirect, request, session
from apps.morse import MorseCodeTranslator
from apps.braille import BrailleTranslator
from apps.mendel import PeriodicTable

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'D5r09fAe+!aIB1eRMT4tO*ko(M.w^s'

@app.route('/', methods=['POST', 'GET'])
def qtools():

    page_head = '''<!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>Quest tools</title>

            <link rel="stylesheet" href="static/bootstrap.css">
            <link rel="stylesheet" href="static/qtools.css">

        </head>
        <span style="float: right"><font size="-1">Версия 0.05</font></span>
        <nav>
            <h2>Quest tools</h2>         
        </nav>
        <body>
        <main>
        '''
    page_foot = '''
        </main>
        </body></html>'''
    input_form = '''
              <form action = "/" method = "post">
                 <p align="right">Азбука Морзе:
                    <input type="text" name="morse_txt" />
                    <input type="submit" name="morse_submit" value="&#9735" title="отправить"/>
                 </p>
                 <p align="right">Шрифт Брайля: <img src="/static/Braille_cell.svg" alt="Braille" width="40" height="56">
                    <input type="text" name="braille_txt" />
                    <input type="submit" name="braille_submit" value="&#9735" title="отправить"/>
                 </p>
                 <p align="right">Таблица Менделеева:
                    <input type="text" name="mendel_txt" />
                    <input type="submit" name="mendel_submit" value="&#9735" title="отправить"/>
                 </p>
                 <p align="right">Алфавит:
                    <input type="text" name="alpha_txt" />
                    <input type="submit" name="alpha_submit" value="&#9735" title="отправить"/>
                 </p>               
                 </form>
                 '''
                 #  <font size="-1">(код, слово кириллицей или латиницей; несколько &#8212 через пробел)</font>
    clear_button = '''
                 <form action = "/" method = "post">
                    <p>Очистить вывод 
                       <input type="submit" name="clear_submit" value="&#9851" title="очистить"/>
                    </p>
                 </form> 
                 '''

    if session.get('output_window') is None:
        output_window = ''
    else:
        output_window = session.get('output_window')

    def add_to_output():
        # updating Output Window
        output_window = session.get('output_window')
        output_window = zapros + '<br>' + output_window
        output_window = otvet + '<br>' + output_window
        session['output_window'] = output_window

    if request.method == 'POST':

        # print(request.form, request.form.get('braille_txt'))

        # Очистка окна вывода
        if 'clear_submit' in request.form:
            session['output_window'] = ""
            return redirect('/')

        # -- --- .-. ... . -.-. --- -.. . .--. .-. --- -.-. . ... ... .. -. --.
        # Morse Code processing
        # -- --- .-. ... . -.-. --- -.. . .--. .-. --- -.-. . ... ... .. -. --.
        if request.form.get('morse_txt'):
            try:
                zapros = request.form['morse_txt']
                if len(zapros) > 0:
                    morse = MorseCodeTranslator()
                    otvet = morse.translate_morse(zapros).replace('\n','<br>')
                    # check for empty result - REVERSE: text to morse convert
                    if otvet == '<br>':
                        otvet = morse.translate_text(zapros)
                    add_to_output()
            except:
                zapros = ''
                otvet = 'Error: сбой блока Morse'
                add_to_output()
            return redirect('/')

        # ⠠⠞⠗⠁⠝⠎⠇⠁⠞⠊⠝⠛ ⠞⠑⠭⠞ ⠖ ⠠⠛⠗⠁⠙⠑ ⠼⠃ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠊⠎ ⠁ ⠝⠕⠝⠤⠞⠗
        # Braille-Translator
        # ⠠⠞⠗⠁⠝⠎⠇⠁⠞⠊⠝⠛ ⠞⠑⠭⠞ ⠖ ⠠⠛⠗⠁⠙⠑ ⠼⠃ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠊⠎ ⠁ ⠝⠕⠝⠤⠞⠗
        if request.form.get('braille_txt'):
            try:
                zapros = request.form['braille_txt']
                if len(zapros) > 0:
                    braille = BrailleTranslator()
                    if zapros.replace(' ','').isnumeric():
                        # цифровые коды Брайля 12 14 и т.п.
                        otvet = braille.convert_codes(zapros).replace('\n','<br>')
                        otvet += '<br> <braille>' + braille.translate_text(otvet.split('<br>')[0]) + '</braille>'
                    else:
                        # просто текст - возвращается код Брайля в UTF-8
                        otvet = '<braille>' + braille.translate_text(zapros) + '</braille>'
                    add_to_output()
            except:
                zapros = ''
                otvet = 'Error: сбой блока Braille'
                add_to_output()
            return redirect('/')

        # H	He	Li	Be	B	C	N	O	F	Ne	Na	Mg	Al	Si	P	S	Cl	Ar
        # Periodic Table Mendeleev
        # H	He	Li	Be	B	C	N	O	F	Ne	Na	Mg	Al	Si	P	S	Cl	Ar
        if request.form.get('mendel_txt'):
            try:
                zapros = request.form['mendel_txt']
                if len(zapros) > 0:
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
                    add_to_output()
            except:
                zapros = ''
                otvet = 'Error: сбой блока Mendeleev'
                add_to_output()
            return redirect('/')

        # ----------абвгдеёжзийклмнопрстуфхцчшщъыьэюя----------
        # Алфавит
        # ----------абвгдеёжзийклмнопрстуфхцчшщъыьэюя----------
        if request.form.get('alpha_txt'):
            try:
                zapros = request.form['alpha_txt']
                otvet = ''
                alphabet_en = '0abcdefghijklmnopqrstuvwxyz'
                alphabet_ru = '0абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                if len(zapros) > 0:
                    if zapros.replace(' ', '').isnumeric():
                        otvet_ru = ''
                        otvet_en = ''
                        for letter_number in zapros.split():
                            letter_number = int(letter_number)
                            otvet_ru += alphabet_ru[letter_number] if letter_number < len(alphabet_ru) else ''
                            otvet_en += alphabet_en[letter_number] if letter_number < len(alphabet_en) else ''
                        otvet = otvet_ru + '<br>' + otvet_en
                    else:
                        for letter in zapros:
                            letter_number = ''
                            letter_number = str(alphabet_ru.index(letter)) if letter in alphabet_ru else ''
                            if letter_number == '':
                                letter_number = str(alphabet_en.index(letter)) if letter in alphabet_en else ''
                            otvet += letter_number + ' '
                    add_to_output()
            except:
                zapros = ''
                otvet = 'Error: сбой блока Alpha'
                add_to_output()
            return redirect('/')

    page = f'{page_head}' \
           '''   <div class="row">
             <div class="column"> ''' \
           f'{input_form} \n' \
           f'</div> <!-- column --> \n' \
           '''<div class="column">''' \
           f'{clear_button} \n' \
           f'<p>{output_window}</p> \n' \
           '</div> <!-- column -->  </div> <!-- row -->' \
           f'{page_foot}'

    return page

if __name__ == '__main__':

    app.run(debug=False)