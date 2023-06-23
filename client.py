from flask import Flask, request, jsonify
import os
import requests
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

# Do not remove this method.
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

@app.route('/igv')
def igv():
    if is_api_testing():
        return mock_responses()
    else:
        tax = get_tax_from_api()
        return jsonify(igv=tax), 200

def is_api_testing():
    return os.getenv("API_TESTING") == "true"

def mock_responses():
    response_code = int(request.args.get('response_code', 200))

    if response_code == 200:
        return jsonify(igv=15), 200
    elif response_code == 403:
        return jsonify(error="Forbidden"), 403
    elif response_code == 500:
        return jsonify(error="Internal Server Error"), 500

def get_tax_from_api():
    url = os.getenv("TAX_API_URL")

    response = requests.get(url)
    data = response.json()

    return int(data["Tax"])

if __name__ == "__main__":
    app.run(debug=True, port=3000)
