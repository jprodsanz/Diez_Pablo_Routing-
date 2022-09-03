from flask import Flask, render_template

app = Flask(__name__)

app.secret_key="el bicho"

@app.route('/')
def home():
    return 'Hello'

@app.route('/ronaldo')
def ninjas():
    return render_template('index.html',ronaldo = True)

@app.route('/ronaldo/<ronaldo_color>')
def color(ronaldo_color):
    return render_template('index.html',ronaldo = False, color = ronaldo_color)

if __name__=="__main__":     
    app.run(debug=True)    