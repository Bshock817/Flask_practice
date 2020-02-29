from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route("/")
def survey_form():
    #print('--------------------\n'*10)
    return render_template('index.html')

@app.route("/submit_survey", methods=['POST'])
def on_submit():
    return render_template("results.html", survey_data = request.form)

if __name__ == "__main__":
    app.run(debug=True)    
