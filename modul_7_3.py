class WordsFinder:
    def __init__(self,*args):
        self.file_names=args
    def get_all_words(self):
        all_words={}
        punkt=[',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
             with open(str(name)) as file:
                 line = file.read().replace('\n', ' ')
                 line = line.lower()
                 result_string = ''.join(char for char in line if char not in punkt)
                 result_string=result_string.split()
                 all_words[name] = result_string
        return all_words
    def find(self, word):
        self.word=word.lower()
        all_words=self.get_all_words()
        found={}
        for f, words in all_words.items():
            index=(words.index(self.word)+1)
            found[f]=index
        return found
    def count(self,word):
        self.word_1=word.lower()
        all_words = self.get_all_words()
        count1={}
        for f, words in all_words.items():
            count_1 = 0
            for i in range(len(words)):
                if self.word_1==words[i]:
                    count_1+=1
            count1[f]=count_1
        return count1

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


# finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('Child')) # 3 слово по счёту
# print(finder2.count('Child')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt','Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))

