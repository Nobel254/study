def single_root_words(root_word, *other_word):
    same_words=[]
    for i in range (len(other_word)):
        root_word1=root_word.lower()
        other_word1=other_word[i].lower()
        if len(root_word1)>len(other_word1):
            if other_word1 in root_word1:
                same_words.append(other_word[i])
        elif len(root_word1)<len(other_word1):
                if root_word1 in other_word1:
                    same_words.append(other_word[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)