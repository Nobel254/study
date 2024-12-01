def single_root_words(root_word, *other_word):
    root_word = str(root_word)
    root_word = root_word.lower()
    other_word_ = []
    slovo = []
    same_words = []
    for i in range(len(other_word)):
        if len(root_word) <= len(other_word[i]):
            other_word_ = str(other_word[i])
            other_word_ = other_word[i].lower()
            for j in range(len(other_word_)):
                if len(other_word_[j:len(root_word) + j]) < len(root_word):
                    break
                slovo.append(other_word_[j:len(root_word) + j])
                world_count = slovo.count(root_word)
            if world_count > 0:
                same_words.append(other_word_)
            slovo.clear()
        else:
            other_word_ = str(other_word[i])
            other_word_ = other_word[i].lower()
            for j in range(len(root_word)):
                if len(root_word[j:len(root_word)]) < len(other_word):
                    break
                slovo.append(root_word[j:len(other_word_) + j])
                world_count = slovo.count(other_word_)
            if world_count > 0:
                same_words.append(other_word_)

        slovo.clear()
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)