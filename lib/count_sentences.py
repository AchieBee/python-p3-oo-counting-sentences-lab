class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            self.value = ''
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = filter(None, re.split(r'[.!?]', self.value))
        return len(list(sentences))
