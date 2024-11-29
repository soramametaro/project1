def str2words(doc, stop):
    words = []
    for token in T.tokenize(doc):
        if token.part_of_speech == '形容詞,自立' or token.part_of_speech == '動詞,自立' or token.part_of_speech == '名詞':
            words.append(token.base_form)
    important_words = [word for word in words if word != stop]
    return important_words
