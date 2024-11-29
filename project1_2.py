def extract_frequent_words(word_frequency, coverage):
    ans = []
    num = 0
    all_num = 0
    for value in word_frequency.values():
        all_num += value
    for k, v in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True):
        num += v
        if (num-v)/all_num < coverage:
            ans.append(k)
        else:
            break
    return ans
