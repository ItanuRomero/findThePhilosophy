import wikipedia
import urllib
import ssl
import re
from cssselect import GenericTranslator, SelectorError
from lxml.etree import fromstring


def searcher(word):
    wikipedia.set_lang('en')
    return wikipedia.search(word, results=3)


def philosophy_finder(page):
    paths = list()
    context = ssl._create_unverified_context()
    try:
        page = wikipedia.page(page)
        next_url = page.url
    except wikipedia.exceptions.DisambiguationError as err:
        next_url = f'https://en.wikipedia.org/wiki/{page}'
    while True:
        print(next_url)
        if next_url.split('/')[-1] == 'Philosophy':
            break
        html = urllib.request.urlopen(next_url, context=context).read()
        article_name = next_url.split('wiki/')[1]
        first_paragraph = str(html).split(f'<p>')[1].split(f'<b>{article_name}')
        first_paragraph = str(first_paragraph).split('</p>')[0]
        try:
            if 'href="#' in first_paragraph:
                first_paragraph = str(first_paragraph).replace('href="#', '')
            ignore_parenthesis = re.sub("[\(\[].*?[\)\]]", "", first_paragraph)
            ignore_parenthesis = str(ignore_parenthesis).split('href="')[1]
            final_link = str(ignore_parenthesis).split('"')[0]
            next_url = f'https://en.wikipedia.org{final_link}'
            paths.append(final_link)
        except IndexError as err:
            return f'Impossible to reach :( - we tried for {len(paths)} pages'
        with open('file.txt', 'a') as filename:
            filename.write(f'{final_link}\n')
    return f'We find after {len(paths)} tries'