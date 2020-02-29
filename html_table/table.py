from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    #print('--------------------\n'*10)
    return "Hello write '/table' in the URL after the 5000!!"

@app.route("/table")
def html_table():
    print('--------------------\n'*10)
    users = [
   {'first_name' : 'Brian', 'last_name' : 'Shockency'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("table.html", user_data = users)

if __name__ == "__main__":
    app.run(debug=True)