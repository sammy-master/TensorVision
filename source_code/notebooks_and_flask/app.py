from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1><p>Welcome to my website!</p>"

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>I am a second-year student learning Flask!</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1><p>Email: student@college.edu</p>"

if __name__ == "__main__":
    app.run(debug=True)