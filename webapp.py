import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #SECRET_KEY is an environment variable.
                                         #The value should be set in Heroku (Settings->Config Vars).

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('rendermain'))

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session['answer1'] = request.form['q1']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    total = 0
    if request.form['q2'] == "false":
        session['response2']="Correct"
        total+=50
    else:
        session['response2']="Incorrect"
    if session['answer1'] == "false":
        session['response1']="Correct"
        total+=50
    else:
        session['response1']="Incorrect"

    return render_template('page3.html')

if __name__=="__main__":
    app.run(debug=False)
