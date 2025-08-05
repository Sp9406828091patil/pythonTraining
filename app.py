from flask import Flask, request, render_template
from machineLearning.loadPickle import predictTitanicSurvivor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html is in a "templates" folder

@app.route('/Aboli', methods=['POST'])
def submit():
    Pclass = request.form['pclass']
    Sex = request.form['sex']
    Age = request.form['age']
    SibSp = request.form['sibSp']
    Parch = request.form['parch']
    Fare = request.form['fare']
    Embarked = request.form['embarked']

    prediction =  predictTitanicSurvivor(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)

    return f"{prediction}!"



if __name__ == '__main__':
    app.run(debug=True)
