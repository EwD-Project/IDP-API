import re
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/v1/convert-text', methods=['POST'])
def convert_text():
	# TODO: update code if needed
	
    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'No text provided'}), 400

    original_text = request.json['text']
    accent = request.json['accent']
    try:
        words_and_infos = preprocess_text(original_text, accent)
        words_and_infos = eds_process(words_and_infos)
        result_text = postprocess_text(original_text, words_and_infos)
        return jsonify({'diacritizedText': result_text}), 200
    # pylint: disable=broad-exception-caught
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def preprocess_text(original_text, accent):
	# TODO: update code
	
    words_and_positions = []
    word_pattern = r'\b\w+\b'

    # Finding words and their positions
    for match in re.finditer(word_pattern, text):
        word_info = {
            'word': match.group(),
            'start_pos': match.start(),
            'end_pos': match.end()
        }
        words_and_positions.append(word_info)


    return words_and_infos


def eds_process(words_and_infos):
    # TODO: implement
    return updated_words_and_infos


def postprocess_text(original_text, words_and_infos):
    # TODO: implement
    return result_text


if __name__ == '__main__':
    app.run(debug=True)
