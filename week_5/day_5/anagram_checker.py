from itertools import permutations

class AnagramChecker:
    def __init__(self,words):
        self.words = open("words.txt", "r").read()
        self.words_list = list(self.words.split("\n"))
        # print(words_list)

    def is_valid_word(self,word):
        for items in self.words_list:
            if word in self.words_list:
                print("valid")
                break
            else:
                print("not valid")
                break

    def get_anagrams(self, word):
        letter_list = list(word)
        permutation_list = permutations(letter_list)
        final_list = list(permutation_list)
        temp = []
        for i in final_list:
            joined = ("".join(i))
            temp.append(joined)
        # print(temp)
        list_of_anagrams = []
        for item in temp:
            if item in self.words_list:
                list_of_anagrams.append(item)
        # print(list_of_anagrams)
        unique_anagram_list = set(list_of_anagrams)
        print(unique_anagram_list)

anagram1 = AnagramChecker("dine")
anagram1.is_valid_word('HELLO')
anagram1.get_anagrams("HEY")
anagram1.get_anagrams("SLEEP")
