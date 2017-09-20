from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/newshoppinglist')
def newshoppinglist():
    return render_template('newshoppinglist.html')

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
