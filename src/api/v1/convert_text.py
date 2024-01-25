from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/v1/convert-text', methods=['POST'])
def convert_text():
    data = request.json
    # Lógica para adicionar diacríticos
    # ...
    # Supondo que `result` seja o texto com diacríticos
    return jsonify(diacritizedText=data), 200


if __name__ == '__main__':
    app.run(debug=True)
