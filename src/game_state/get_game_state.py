from flask import Flask, request, jsonify

app = Flask(__name__)

# This retrieves the input and returns the processed output


@app.route('/process', methods=['POST'])
def process_request():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    input = data['input_string']

    output = 'Hello World'  # This is where the processing will be called

    return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)
