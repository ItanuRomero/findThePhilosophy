from flask import Flask
from philosophy_finder import searcher, philosophy_finder
from getting_to_philopy import start

app = Flask(__name__)


@app.route("/")
def index():
    page_list = searcher("data")
    link = f'https://en.wikipedia.org/wiki/{page_list[0]}'
    url, how_many_times = start(link)
    return f'returned from {url} path:\n{how_many_times}'


app.run()
