from flask import Flask, render_template

app = Flask(__name__) # To indicate that this file is the main file

app.config["STATIC_FOLDER"] = 'static'

@app.route('/')
def default():    
    return render_template('home.html')

@app.route('/admin')
def about():
    return render_template('admin.html')

@app.route('/user/<name>')
def member(name):
    return "<h1>Hello, {}</h1>".format(name)

if __name__ =="__main__":
    app.run(debug=True)
