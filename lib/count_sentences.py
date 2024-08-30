class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
            self._value = ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        import re

        # Replace multiple punctuation marks with a single one
        cleaned_text = re.sub(r'[!?.]+', '.', self._value)

        # Split by periods, question marks, or exclamation marks
        sentences = re.split(r'[.?!]', cleaned_text)

        # Filter out empty strings from the result of split
        sentences = [s.strip() for s in sentences if s.strip()]

        return len(sentences)
