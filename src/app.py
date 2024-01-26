import re
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger

from enums.accent import Accent
from services.phonetics_service import PhoneticsService
from services.text_service import TextService

app = Flask(__name__)
swagger = Swagger(app)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # URL for swagger.json
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "IDP API"}
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


text_service = TextService()


@app.route('/api/v1/get-phonefied-text', methods=['POST'])
def get_phonefied_text():
    """
    Returns the phonemized version of the provided text.
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            text:
              type: string
              example: "Hello world"
            accent:
              type: string
              example: "en-us"
        required: true
    responses:
      200:
        description: Successful response
      400:
        description: Bad request
      500:
        description: Internal server error
    """
    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'No text provided'}), 400

    text = request.json['text']
    accent = request.json.get('accent', 'en-us')

    try:
        result = PhoneticsService.phonefy_text(text, accent)
        return jsonify({'phonefied_text': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/v1/convert-text', methods=['POST'])
def convert_text():
    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'No text provided'}), 400

    original_text = request.json['text']
    accent = request.json.get('accent', 'en-us')

    try:
        result_text = text_service.convert_text(original_text, accent)
        return jsonify({'converted_text': result_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
