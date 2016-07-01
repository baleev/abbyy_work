import nltk


class TextInfo:
    text = ''
    length = 0
    dialog_percentage = 0.0
    dialog_count = 0
    quote_precentage = 0.0
    quote_count = 0
    date_percentage = 0.0
    named_entity_percentage = 0.0
    sentence_max_length = 0
    sentence_avg_length = 0.0
    exclamation_sentence_count = 0
    sentence_list = []
    sentence_count = 0

    # Узнаём длину текста
    def init_length(self):
        self.length = len(self.text)

    # Определяем количесвто предложений и парсим всё в лист
    def init_sentence_count(self):
        self.sentence_list = list(nltk.sent_tokenize(self.text, language='russian'))
        self.sentence_count = len(self.sentence_list)

    # Получаем инфу по предложениям (средняя длина, кол-во восклицательных, кол-во цитат)
    def init_sentence(self):
        max = 0
        for i in self.sentence_list:
            if len(i) > max:
                max = i
            if i[len(i - 1)] or i[len(i - 2)] == '!':
                self.exclamation_sentence_count += 1
            if i[0] == '"' and i[len(i - 1)] == '"':
                self.quote_count += 1
            if i[0] == '-':
                self.dialog_count += 1
        self.sentence_avg_length = self.length / self.sentence_count
        self.sentence_max_length = max
        self.quote_precentage = self.quote_count / self.sentence_count
        self.dialog_percentage = self.dialog_count / self.sentence_count

    def __init__(self, text):
        self.text = text
        self.init_sentence_count()
        self.init_sentence()
