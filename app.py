from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')  # This loads your HTML file

if __name__ == '__main__':
    app.run(debug=True)
