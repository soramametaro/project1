def words2vec(words, frequent_words):
    counter = {}
    for fw in frequent_words:
        counter[fw] = 0
    for w in words:
        if w in counter:
            counter[w] += 1
    vec = []
    for i in range(len(frequent_words)):
        vec.append(counter[frequent_words[i]])
    return vec
