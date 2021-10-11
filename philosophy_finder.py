import wikipedia


def searcher(word):
    wikipedia.set_lang('en')
    return wikipedia.search(word, results=3)


def philosophy_finder(page):
    visited_pages = list()
    try:
        page = wikipedia.page(page)
    except wikipedia.DisambiguationError as error:
        page = wikipedia.page(error.options[0])
    print(page.url)
    while True:
        try:
            visited_pages.append(page)
            print(page.url)
            if 'Philosophy' in page.links or len(visited_pages) == 10:
                break
            page_list = searcher(page.links[0])
            counter = 0
            while page in visited_pages:
                counter += 1
                try:
                    page = wikipedia.page(page_list[counter])
                except wikipedia.DisambiguationError as error:
                    page = wikipedia.page(error.options[0])
                except IndexError as error:
                    page_list = searcher(page_list[counter - 1])
                    page = wikipedia.page(page_list[0])
        except Exception as error:
            print(error)
            return f'We failed at {len(visited_pages)} tries'
    return f'We find Philosophy at {len(visited_pages)} tries'
