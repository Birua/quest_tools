import gzip
import re

class MaskSearch:
    """ Поиск по простой маске
        ? - одна непустая буква
        * - несколько букв или пусто
    Методы:
        mask_search_ru(str) => str
        mask_search_en(str) => str
    """
    def __init__(self):
        pass

    def filter_by_pattern(self, elements, pattern):
        pattern = pattern.lower().strip()
        # convert `?` and `*` flags
        pattern = pattern.replace('?', '.').replace('*', '.*?')
        # flags startwith and endwith
        pattern = '^' + pattern + '$'
        return sorted([substring for substring in elements if re.match(pattern, substring)])

    def _mask_search(self, words_set, pattern):
        match_list = self.filter_by_pattern(words_set, pattern)
        if len(match_list) > 100:
            output_str = pattern + ' => (>100!) ' + ', '.join(match_list[:100])
        else:
            output_str = pattern + f' => ({len(match_list)}) ' + ', '.join(match_list)
        return output_str

    def mask_search_ru(self, pattern):
        with gzip.open('static/russian.txt.gz', 'r') as f:
            self.russian_words = set(f.read().decode('cp1251').lower().split())
        return self._mask_search(self.russian_words, pattern)

    def mask_search_en(self, pattern):
        with open('static/english_alpha.txt') as word_file:
            self.english_words = set(word_file.read().lower().split())
        return self._mask_search(self.english_words, pattern)

if __name__ == '__main__':
    import time

    start = time.time()
    mask = MaskSearch()
    print(mask.mask_search_ru('?лов?'))
    print(mask.mask_search_ru('лов*'))
    print(mask.mask_search_en('en?r??'))
    print(mask.mask_search_en('*ergy'))
    print(f'time: {(time.time() - start):.3f}')