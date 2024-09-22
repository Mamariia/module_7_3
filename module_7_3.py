class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = [*file_name]

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()  # Возвращает строку в нижнем регистре
                    chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for char in chars:  # Удаление символов из строки
                        line = line.replace(char, ' ')
                    line = line.split()  # Разбивает строку на элементы списка
                    words.extend(line)  # Добавляет все слова из файла в единый список
                all_words[name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                index = words.index(word) + 1
                result[name] = index
                continue
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            counter = words.count(word)
            result[name] = counter
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего