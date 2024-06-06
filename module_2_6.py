def single_root_words(root_word, *other_words):
    same_words = []
    low_root = root_word.lower()
    for i in other_words:
        low = i.lower()
        if low.count(low_root) != 0 or low_root.count(low) != 0:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
