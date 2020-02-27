from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'counter'

@app.route("/")
def server_on():
    if "visits" not in session:
        session['visits'] = 0
    else:
        session['visits'] = session['visits'] + 1
    return render_template("counter.html")

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)