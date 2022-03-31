import re


def extraction_of_words(word_list):

    quoted_phrases = word_list.split('"')[1::2]
    if len(quoted_phrases) > 0:
        for q in quoted_phrases:
            word_list = word_list.replace(q, '').replace('"', '').strip()
    else:
        quoted_phrases = word_list.split("'")[1::2]
        for q in quoted_phrases:
            word_list = word_list.replace(q, '').replace("'", '').strip()

    # replace word_list delimeter with pipe
    word_list = word_list.replace(" ", "|").replace(",", "|")
    for w in word_list.strip().split("|"):
        if w != '':
            quoted_phrases.append(w)
    return quoted_phrases


def replace_words(censoredWords_list, document_text):
    regex = re.compile('|'.join(map(re.escape, censoredWords_list)))
    the_document = regex.sub("XXXX", document_text)
    return the_document