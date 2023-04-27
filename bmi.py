from flask import Flask, jsonify, request

app = Flask(__name__)

def calculate_bmi(weight: float, height: float) -> float:
    bmi = weight / (height ** 2)
    return round(bmi, 2)

@app.route('/bmi', methods=['POST'])
def calculate_bmi_route():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height'])
    bmi = calculate_bmi(weight, height)
    return jsonify({'bmi': bmi})

if __name__ == '__main__':
    app.run(debug=True)
