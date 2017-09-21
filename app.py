from models.model import *
from flask import Flask, render_template,redirect, request,url_for

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if username == user.username:
                if password == user.password:
                    
                    return redirect(url_for('dashboard'))
                else:
                    if username or password:
                        return redirect(url_for('/'))
    return render_template("index.html")

   

@app.route('/register',methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(firstname,lastname,username,email,password)
        users.append(user)     
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/dashboard' ,methods=['POST','GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/newshoppinglist' ,methods=['POST','GET'])
def newshoppinglist():
    if request.method == 'POST':
        shoppinglist = request.form['shoppinglist']
        description = request.form['description']
        items = request.form['items']
        status = request.form['status']
        dateadded = request.form['dateadded']
        shoppinglist = Shoppinglist(shoppinglist,description,items,status,dateadded)
        shopping_list.append(shoppinglist)
        return render_template("fullList.html", shopping_list = shopping_list)
    return render_template("newshoppinglist.html")

@app.route('/fullList')
def fullList():
    return render_template('fullList.html')    

@app.route('/editlist')
def editlist():
    return render_template('editlist.html')

@app.route('/deletelist')
def deletelist():
    return render_template('deletelist.html')

if __name__ == '__main__':
    app.run(debug=True)
