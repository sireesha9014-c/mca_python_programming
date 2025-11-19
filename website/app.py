from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🏠 Welcome Home!"

@app.route('/about')
def about():
    return "This is the About page of the website."

@app.route('/contact')
def contact():
    return "📧 Contact: email@example.com"

if __name__ == '__main__':
    app.run(debug=True)
