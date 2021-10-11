from flask import Flask
from philosophy_finder import searcher, philosophy_finder

app = Flask(__name__)


@app.route("/")
def index():
    page_list = searcher("math")
    print(page_list)
    how_many = philosophy_finder(page_list[0])
    return f'Trying to find philosophy: {how_many}'


app.run()
