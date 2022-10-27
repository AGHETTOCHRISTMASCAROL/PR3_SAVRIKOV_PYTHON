import sys

class FileAnalytics():
    """Аналитика файла"""

    def __init__(self, file_name):
        self.file_name :str = file_name
        self.char_count :int = 0
        self.min_length_word :int = sys.maxsize
        self.max_length_word :int = sys.maxsize * -1
        self.middle_length_word :float = 0
        self.vowels_letters_count :int = 0
        self.consonants_letters_count :int = 0
        self.repetitions_length_words :dict = {}
        self.analytics_outpute :str = ''

    def get_count_char(self, line):
        self.char_count += len(line)

    def get_max_length_word(self, line):
        if len(line) > self.max_length_word:
            self.max_length_word = len(line)

    def get_min_length_word(self, line):
        if len(line) < self.min_length_word:
            self.min_length_word = len(line)

    def get_count_vowels(self, line):
        vowels :set = set('aeiouyAEIOUY') #'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
        for letter in line:
            if letter in vowels:
                self.vowels_letters_count += 1
    
    def get_count_consonants(self, line):
        consonants :set = set('bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ') #'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
        for letter in line:
            if letter in consonants:
                self.consonants_letters_count += 1

    def get_repetitions_legth_words(self, line):
        if len(line) in self.repetitions_length_words.keys():
            self.repetitions_length_words[len(line)] += 1
        else:
            self.repetitions_length_words[len(line)] = 1

    def get_middle_length_word(self, count_words):
        self.middle_length_word = self.char_count/count_words
    
    def generation_analytics_for_outpute(self):
        self.analytics_outpute = f"""{'*' * 100}\n
\tАналитика Файла {self.file_name}\n
{'*' * 100}\n
1. Всего символов --> {self.char_count}
2. Максимальная длина слова --> {self.max_length_word}
3. Минимальная длина слова --> {self.min_length_word}
4. Средняя длина слова --> {round(self.middle_length_word, 2)}
5. Количество гласных --> {self.vowels_letters_count}
6. Количество согласных --> {self.consonants_letters_count}
7. Количество повторений слов с одной длиной:\n\n"""

        sorted_tuple = sorted(self.repetitions_length_words.items(), key=lambda t: t[0]) #Сортировка словаря с повторениями длин слов
        self.repetitions_length_words = dict(sorted_tuple)

        for item in sorted_tuple:
            self.analytics_outpute += f'\t{item[0]} симв. >> {item[1]} повт.\n'

    def print_analytics_in_console(self):
        print(self.analytics_outpute)
    
    def create_file_analytics(self):
        with open(f'Analytics for {self.file_name}', 'w', encoding='utf-8') as file:
            file.write(self.analytics_outpute)

    def get_analytics(self):
        with open(self.file_name, 'r') as file:
            for count, line in enumerate(file, start=1):
                line = line.rstrip()
                self.get_count_char(line)
                self.get_max_length_word(line)
                self.get_min_length_word(line)
                self.get_count_vowels(line)
                self.get_count_consonants(line)
                self.get_repetitions_legth_words(line)

        self.get_middle_length_word(count)
        self.generation_analytics_for_outpute()
        self.print_analytics_in_console()
        self.create_file_analytics()