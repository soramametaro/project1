def str2words(doc, stop):
    important_words = []
    for token in T.tokenize(doc):
        if '形容詞,自立' in str(token.part_of_speech) or '動詞,自立' in str(token.part_of_speech) or '名詞' in str(token.part_of_speech):
            important_words.append(token.base_form)
    for stop_word in stop:
        if stop_word in important_words:
            important_words.remove(stop_word)
    return important_words
