import os

from initiate_index import initiate_index
from flask import Flask, request
from create_or_update import create_or_update_index
from pydantic_models import Document, Question


app = Flask(__name__)


@app.route("/add_document", methods=["POST"])
def add_document():
    document = Document(**request.json)
    if create_or_update_index(document.filename, document.content):
        return 'Index created', 200
    else:
        return 'file should be txt format', 400


@app.route('/question', methods=['GET'])
def question():
    os.environ["OPENAI_API_KEY"] = 'Your API Key'  # I sincirely couldn't figure out how to integrate this API key to instantiate index. Constantly getting code 429
    query = Question(**request.args)
    index = initiate_index()
    query_engine = index.as_query_engine()  # by that we're creating a sort of the concrete for our queries to be analized
    query_result = query_engine.query(query.question)  # placing user's question to the query engine
    return {
        "result": query_result.response  # returning the result
    }, 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)
