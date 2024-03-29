from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return "This is about page"

@app.route('/contact')
def contact_page():
    return "This is contact page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)