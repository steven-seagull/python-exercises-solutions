sep_words = input()

sep_words_lst = sep_words.split(' ')
sep_words_lst.sort()
set_words = set(sep_words_lst)

print(' '.join(set_words))

