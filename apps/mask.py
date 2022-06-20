import gzip
import re
import sqlite3


class MaskSearch:
    """Поиск по простой маске
        ? - одна непустая буква
        * - несколько букв или пусто
    Методы:
        mask_search_ru(str) => str
        mask_search_en(str) => str
        mask_search_ru_SQL(str) => str
        mask_search_en_SQL(str) => str
    """

    def __init__(self):
        pass

    def filter_by_pattern(self, elements, pattern):
        pattern = pattern.lower().strip()
        # convert `?` and `*` flags
        pattern = pattern.replace("?", ".").replace("*", ".*?")
        # flags startwith and endwith
        pattern = "^" + pattern + "$"
        return sorted(
            [substring for substring in elements if re.match(pattern, substring)]
        )

    def _mask_search(self, words_set, pattern):
        match_list = self.filter_by_pattern(words_set, pattern)
        if len(match_list) >= 100:
            output_str = pattern + " => (>100!) " + ", ".join(match_list[:100])
        else:
            output_str = pattern + f" => ({len(match_list)}) " + ", ".join(match_list)
        return output_str

    def mask_search_ru(self, pattern):
        with gzip.open("static/russian.txt.gz", "r") as f:
            self.russian_words = set(f.read().decode("cp1251").lower().split())
        return self._mask_search(self.russian_words, pattern)

    def mask_search_en(self, pattern):
        with open("static/english_alpha.txt") as word_file:
            self.english_words = set(word_file.read().lower().split())
        return self._mask_search(self.english_words, pattern)

    def mask_search_en_SQL(self, pattern):
        # Connecting to the database
        connection = sqlite3.connect("static/eng_words.db")
        cursor = connection.cursor()
        pattern = pattern.lower().strip()
        word_mask = pattern.replace("?", "_").replace("*", "%")
        select_all = f"SELECT words FROM eng_words \
                      WHERE words LIKE '{word_mask}' \
                      LIMIT 100"
        rows = cursor.execute(select_all).fetchall()
        output_str = pattern + " => " + f"({len(rows)}) "
        output_str += ", ".join([word[0] for word in rows])
        connection.close()

        return output_str

    def mask_search_ru_SQL(self, pattern):
        # Connecting to the database
        connection = sqlite3.connect("static/rus_words.db")
        cursor = connection.cursor()
        pattern = pattern.lower().strip()
        word_mask = pattern.replace("?", "_").replace("*", "%")
        select_all = f"SELECT words FROM rus_words \
                      WHERE words LIKE '{word_mask}' \
                      LIMIT 100"
        rows = cursor.execute(select_all).fetchall()
        output_str = pattern + " => " + f"({len(rows)}) "
        output_str += ", ".join([word[0] for word in rows])
        connection.close()

        return output_str

    def mask_search_ua_SQL(self, pattern):
        # Connecting to the database
        connection = sqlite3.connect("static/ua_words.db")
        cursor = connection.cursor()
        pattern = pattern.lower().strip()
        word_mask = pattern.replace("?", "_").replace("*", "%")
        select_all = f"SELECT words FROM ua_words \
                      WHERE words LIKE '{word_mask}' \
                      LIMIT 100"
        rows = cursor.execute(select_all).fetchall()
        output_str = pattern + " => " + f"({len(rows)}) "
        output_str += ", ".join([word[0] for word in rows])
        connection.close()

        return output_str


if __name__ == "__main__":
    import time

    start = time.time()
    mask = MaskSearch()
    # print(mask.mask_search_ru('?лов?'))
    # print(mask.mask_search_ru('лов*'))
    # print(mask.mask_search_en('en?r??'))
    print(mask.mask_search_en("*ergy"))
    print(f"time CSV: {(time.time() - start):.3f}")
    start = time.time()
    print(mask.mask_search_en_SQL("*ergy"))
    print(f"time SQL: {(time.time() - start):.3f}")
    start = time.time()
    print(mask.mask_search_ru_SQL("?лов?"))
    print(f"time SQL: {(time.time() - start):.3f}")
    start = time.time()
    print(mask.mask_search_ua_SQL("?лов?"))
    print(f"time SQL: {(time.time() - start):.3f}")
