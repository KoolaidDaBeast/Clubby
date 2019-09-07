from flask import Flask, render_template, Response, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('web_form.html')

app.run(debug=True)
    