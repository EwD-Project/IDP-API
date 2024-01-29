"""
IDP API Main Module

This module defines the Flask application for the Intelligent Diacritic Placer (IDP) API.
The API provides services for converting Standard English text to English with Diacritics (EwD) 
and retrieving the phonetic representation of English text based on a specified accent.

The module sets up the Flask application, configures Swagger for API documentation, 
and defines the routes for the API's endpoints.

Endpoints:
    - GET /api/v1/get-phonetized-text: Returns the phonetic representation (phones) 
      of a given English text based on a specified accent.
    - POST /api/v1/convert-en-to-ewd: Converts Standard English text to English with Diacritics (EwD).

The Flask application is configured to provide Swagger-based documentation under the '/swagger' route.

Usage:
    The application can be run locally by executing the module, which starts the Flask development server.
    It can also be deployed as part of a larger web application stack.

Dependencies:
    - Flask: Web framework used to define and handle API routes.
    - Flasgger: Extension for Swagger documentation.
    - PhoneticsService: Service for phonetic conversion of text.
    - TextService: Service for converting Standard English to EwD.
"""

from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint   # type: ignore
from flasgger import Swagger   # type: ignore

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


@app.route('/api/v1/get-phonetized-text', methods=['POST'])
def get_phonetized_text():
    """
    Returns the phonetized version of the provided text.
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
        result = PhoneticsService.phonetize_text(text, accent)
        return jsonify({'phonetized_text': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/v1/convert-en-to-ewd', methods=['POST'])
def convert_en_to_ewd():
    """
    Converts Standard English text to English with Diacritics (EwD).
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            text:
              type: string
              description: Standard English text to be converted
              example: "This is a test."
            accent:
              type: string
              description: English accent to be used for conversion
              example: "en-us"
        required: true
    responses:
      200:
        description: Text successfully converted to EwD
        schema:
          type: object
          properties:
            converted_text:
              type: string
              example: "Thĭs ĭs ă tĕst."
      400:
        description: Bad request - Text not provided or invalid format
      500:
        description: Internal server error
    """
    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'No text provided'}), 400

    input_text = request.json['text']
    accent = request.json.get('accent', 'en-us')

    try:
        result = text_service.convert_en_to_ewd(input_text, accent)
        return jsonify({'converted_text': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
