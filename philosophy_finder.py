import wikipedia


def searcher(word):
    wikipedia.set_lang('en')
    return wikipedia.search(word, results=3)