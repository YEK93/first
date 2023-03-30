from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_python():
    return "<p>Hello, Python!</p>"

@app.route("/name/<name>")
def name(name):
    print('Type:',type(name))
    return name

@app.route("/number/<int:number>")
def number(number):
    print('Type:',type(number))
    return f"{number}"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)