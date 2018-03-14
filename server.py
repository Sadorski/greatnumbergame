from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "RandomString"
import random
@app.route('/')
def index():
    if not session.get('rando'):
       
        session['rando'] = random.randrange(0,101)
        print "setting rando", session['rando']
    
   

    return render_template('index.html')

@app.route("/results", methods=["POST"])
def answer():
    session['guess'] = request.form['guess']
    print "the guess", (request.form['guess'])
    y = int(session['guess'])  
    x = session['rando']
    if x > y:
        session['id'] = "low"
    elif x < y:
        session['id'] = "high"
    else:
        session['id']= "correct"

    print session['id']

    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

    

app.run(debug=True)