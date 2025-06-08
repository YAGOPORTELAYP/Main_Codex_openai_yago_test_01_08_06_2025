from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json() or {}
    text = data.get('text', '')
    return jsonify({'reply': f"You said: {text}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
