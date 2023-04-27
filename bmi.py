from flask import Flask, jsonify, request

app = Flask(__name__)

def calculate_bmi(weight: float, height: float) -> float:
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def cal_bmr(weight,height,age,gender):
    if gender == 'M':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    return bmr


def calorie_intake(bmr,fitness_goal):
    if fitness_goal == 'weight loss':
        calorie_in = bmr * 0.8
    else:
        calorie_in = bmr * 1.2

    return calorie_in

def classification(bmi):
    if bmi < 18.5:
        bmi_category = 'underweight'
    elif bmi < 25:
        bmi_category = 'normal'
    elif bmi < 30:
        bmi_category = 'overweight'
    else:
        bmi_category = 'obese'

    return bmi_category



@app.route('/bmi', methods=['POST'])
def calculate_bmi_route():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height'])
    gender = data['gender']
    age = int(data['age'])
    fitness_goal = data['fitness_goal']
    bmi = calculate_bmi(weight, height)
    bmr = cal_bmr(weight,height,age,gender)
    cal_intake = calorie_intake(bmr,fitness_goal)
    classi = classification(bmi)


    return jsonify({'bmi': bmi, 'gender': gender,'fitness_goal': fitness_goal, 'bmi': bmi, 'classification': classi, 'cal intake': cal_intake })
if __name__ == '__main__':
    app.run(debug=True)

    
