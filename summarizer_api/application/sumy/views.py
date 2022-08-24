from flask import Blueprint, jsonify, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk

sumy_blueprint = Blueprint("sumy", __name__)
nltk.download('punkt')


@sumy_blueprint.route("/sumy", methods=["post"])
def post():
    json_data = request.get_json()

    text = json_data['text']
    lang = json_data.get('lang', 'english')
    sentences_count = json_data.get('sentencesCount', 10)

    parser = PlaintextParser.from_string(text, Tokenizer(lang))
    stemmer = Stemmer(lang)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(lang)

    data = [str(sentence) for sentence in summarizer(parser.document, sentences_count)]

    response = dict(data=data)
    return jsonify(response)
