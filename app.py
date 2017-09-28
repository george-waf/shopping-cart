from models.model import *
from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=['POST','GET'])
def index():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if (username == user.username) and (password == user.password):
                session['logged_in'] = True
                session['id'] = username
                return redirect(url_for('dashboard'))

    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(firstname, lastname, username, email, password)
        users.append(user)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html', list_items=shopping_list)

@app.route('/newshoppinglist', methods=['POST','GET'])
def newshoppinglist():

    if request.method == 'POST':
        shoppinglist = request.form['shoppinglist']
        description = request.form['description']
        items = request.form['items']
        status = ['status']
        dateadded = ['dateadded']
        slist = Shoppinglist(shoppinglist, description,
                             items, status, dateadded)
        shopping_list.append(slist)
        return redirect(url_for('fullList'))
    return render_template("newshoppinglist.html")

@app.route('/fullList', methods=['POST','GET'])
def fullList():
    return render_template('fullList.html', list_items=shopping_list)

@app.route('/editlist', methods=['POST', 'GET'])
def editlist():
    
    if request.method == 'POST' and request.form.get('edit'):
        item_edit = None
        listid = int(request.form.get('shoppinglist_id'))

        for item in shopping_list:
            if item.listid == listid:
                item_edit = item
                return render_template("editlist.html", item=item_edit)

    if request.method == 'POST' and request.form.get('delete'):
        listid = int(request.form.get('shoppinglist_id'))

        for item in shopping_list:
            if item.listid == listid:
                shopping_list.remove(item)
                return render_template("fullList.html", list_items=shopping_list)

    if request.method == 'POST' and request.form.get('update'):
        item_edit = None
        listid = int(request.form.get('shoppinglist_id'))

        for item in shopping_list:
            if item.listid == listid:
                item.shoppinglist = request.form.get('shoppinglist')
                item.description = request.form.get('description')
                item.items = request.form.get('items')
                item.status = request.form.get('status')
                return render_template("fullList.html", list_items=shopping_list)

    if request.method == 'POST':
        shoppinglist = request.form['shoppinglist']
        description = request.form['description']
        items = request.form['items']
        status = request.form['status']
        dateadded = request.form['dateadded']
        slist = Shoppinglist(shoppinglist, description,
                             items, status, dateadded)
        shopping_list.append(slist)
        return render_template("fullList.html", list_items=shopping_list)   
    return render_template("editlist.html", item=item_edit)             
        
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
