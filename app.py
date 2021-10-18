from flask import Flask, request, jsonify
from philosophy_finder import searcher
from flask_cors import CORS
from getting_to_philopy import start
import re

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return jsonify(
        be_welcome='Hi, this app will try to find Philosophy on wikipedia pages',
        inspiration='https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy',
        message='Please read the docs to use',
        the_docs="https://github.com/ItanuRomero/findThePhilosophy",
    )


@app.route("/howManyTimes", methods=['GET'])
def how_many_times():
    first_page = request.args.get('article')
    if first_page:
        page_list = searcher(first_page)
        link = f'https://en.wikipedia.org/wiki/{page_list[0]}'
        url, path = start(link)
        path = re.sub(r'[()]', '', str(path)).replace('[', '')\
            .replace(']', '')\
            .replace("'", '')\
            .replace('1', 'Philosophy!!')\
            .split(', ')
        print(path)
        response = jsonify(
            first=url,
            how_many_pages=len(path)+1,
            pages=path,
        )
        return response
    else:
        return jsonify(
            error='Insert the article name on URL',
            see_docs="https://github.com/ItanuRomero/findThePhilosophy",
        )


app.run()
CORS(app)
