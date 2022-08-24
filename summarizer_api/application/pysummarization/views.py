from flask import Blueprint, jsonify, request
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

pysummarization_blueprint = Blueprint("pysummarization", __name__)


@pysummarization_blueprint.route("/pysummarization", methods=["post"])
def post():
    json_data = request.get_json()

    text = json_data['text']

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    if json_data.get('lang') == 'ja':
        # Set tokenizer for Japanese.
        auto_abstractor.tokenizable_doc = MeCabTokenizer()
        # Set delimiter for making a list of sentence.
        auto_abstractor.delimiter_list = ["。", "\n"]
    else:
        # Set tokenizer.
        auto_abstractor.tokenizable_doc = SimpleTokenizer()
        # Set delimiter for making a list of sentence.
        auto_abstractor.delimiter_list = [".", "\n"]
    # Summarize document.
    data = auto_abstractor.summarize(text, abstractable_doc)

    response = dict(data=data)
    return jsonify(response)
