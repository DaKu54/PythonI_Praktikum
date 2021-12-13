import collections
from collections import Counter
import re
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"

WORD = 'Dieser Text ist nur ein Test!'

def read_words(file_to_clean):
    with open(file_to_clean, 'r') as file:
        data = file.read().replace('\n', '')
        data = data.replace(" ", "")

    data = ''.join([i for i in data if not i.isdigit()])
    data = data.upper()

    cleaned_words = re.findall('[A-ZÄÜÖ]', data)

    return cleaned_words

def least_used_letter(file_to_investigate):
    word_list = read_words(file_to_investigate)
    print(word_list)

    all_freq = {}
    for i in word_list:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    res = min(all_freq, key=all_freq.get)

    print(res)
    #res = Counter(word_list)
    #res = min(res, key=res.get)
    #least_common = collections.Counter(word_list).most_common()[-1]
    #print(least_common)

least_used_letter('./files/words.txt')