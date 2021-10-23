from flask import Flask , render_template, request

app = Flask(__name__)
import churn as c


@app.route("/" , methods = ['GET','POST'])

def hello():
    if request.method == "POST":
        Geography = request.form['Geography']
        Gender = request.form['Gender']
        age = request.form['age']
        tenure = request.form['tenure']
        balance = request.form['balance']
        products = request.form['products']
        credit_card = request.form['credit_card']
        active_member = request.form['active_member']
        estimated_salary = request.form['estimated_salary']

        churn_pred = c.churn_prediction(Geography,Gender,age,tenure,balance,products,credit_card,active_member,estimated_salary)
        cp = churn_pred
    
    return render_template('index.html' , your_churn = cp)

# @app.route("/sub",methods=['POST'])

# def submit():
#     #html -> .py
#     if request.method == "POST":   # why POST bcoz in index.html we have created form with method POST same take here 
#         return request.form["username"]  # ["username"] --> dictionary

#     #.py -> html
#     return render_template("sub.html", n = name)


if __name__ == "__main__":
    app.run(debug=True)