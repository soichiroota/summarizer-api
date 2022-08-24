from flask import Blueprint, jsonify, request
from summarizer_api.summarizer.summpy.lexrank import summarize

summpy_blueprint = Blueprint("summpy", __name__)


@summpy_blueprint.route("/summpy", methods=["post"])
def post():
    json_data = request.get_json()

    text = json_data['text']
    sent_limit = json_data.get('sentLimit', 5)
    sentences, debug_info = summarize(
        text, sent_limit=sent_limit, continuous=True, debug=True
    )

    response = dict(data=debug_info)
    return jsonify(response)
