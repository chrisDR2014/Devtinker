from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/destinations/')
def destination():
    return render_template('destination.html')

@app.route('/boda/')
def boda():
    return render_template('boda.html')

if __name__ == '__main__':
    app.run()
    #app.run(host="0.0.0.0", debug=True, port=8000)