from flask import Flask
app = Flask(__name__)

@app.route('/') #/ front door (home page)
def home(): # function name (can be anything)
    return "Home Page!" #what visitors see

@app.route('/')
def about():
    # return "About Page!"
    return """<h1>Welcome</h1>
    <p>This is my first website</p>
    """

@app.route('/')
def contact():
    return "Contact Page!"

app.run(debug=True)