from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the Calculator App!"

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        result = num1 + num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        result = num1 - num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
