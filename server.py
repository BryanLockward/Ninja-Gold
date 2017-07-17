from flask import Flask, render_template, redirect, session, request, flash
import random

app=Flask(__name__)
app.secret_key="key"

@app.route('/')
def index():
    try:
        print session['gold']
    except:
        session['gold']=0

    return render_template("index.html",gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process_money():

    if request.form['submit']=='Farm Gold':
        count=random.randint(10,20)
        print count
        p="You made " + str(count) + " gold at the farm"
        try:
            session['msg'].append(p)
        except:
            session['msg']=[p]
        flash(session['msg'])

        session['gold']+=count

    elif request.form['submit']=='Cave Gold':
        count=random.randint(5,11)
        print count
        p="You made " + str(count) + " gold at the cave"
        try:
            session['msg'].append(p)
        except:
            session['msg']=[p]
        flash(session['msg'])
        session['gold']+=count

    elif request.form['submit']=='House Gold':
        count=random.randint(2,5)
        p="You made " + str(count) + " gold at the house"
        try:
            session['msg'].append(p)
        except:
            session['msg']=[p]
        flash(session['msg'])
        session['gold']+=count

    else:
        count=random.randint(-50,50)
        p="You made " + str(count) + " gold at the farm"
        try:
            session['msg'].append(p)
        except:
            session['msg']=[p]
        flash(session['msg'])
        session['gold']+=count

    return redirect('/')

@app.route('/reset',methods=['POST'])
def reset():
    session['gold']=0
    session['msg']=[]
    return redirect('/')
app.run(debug=True)
