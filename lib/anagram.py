


class Anagram:
    def __init__(self, word):
        self._word = word

    def match(self, word_list):
        result = []
        for l in word_list:
            sorted([letter for letter in l])
            if sorted([letter for letter in self._word]) == sorted([letter for letter in l]):
                result.append(l)
        return result 
        