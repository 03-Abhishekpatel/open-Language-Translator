from flask import Flask, render_template,request

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
