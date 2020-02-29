from flask import Flask, redirect, render_template, session, request
from random import randrange
from datetime import datetime
app = Flask(__name__)
app.secret_key = "soup"

@app.route("/")
def server_working():
    if 'gold' not in session:
        session['gold'] = 0
    
    if 'activity_log' not in session:
        session['activity_log'] = []


    return render_template("index.html")

@app.route("/process_money", methods =["post"])
def process_money():
    building = request.form.get('building')
    gold = 0
    if building == "farm":
        gold = randrange(10,20)
        session ['gold']  += gold
    elif building == "cave":
         gold = randrange(5,10)
         session ['gold']  += gold
    elif building == "house":
         gold = randrange(2,5)
         session ['gold']  += gold
    elif building == "casino":
         gold = randrange(-50,50)
         session ['gold']  += gold
    
    if gold < 0:
        session['activity_log'].insert(0, f"Entered a casino and lost {gold}! ({datetime.now()})")
    else:
        session['activity_log'].insert(0,f"Earned {gold} from the {building}! ({datetime.now()})")


    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)