from flask import Flask, render_template, request, url_for
import requests
import json
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/captcha')
def captcha():
    return render_template('captcha.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/verify', methods=['POST'])
def verify():
    token = json.loads(request.data)
    
    # FIXME: should be in yaml files
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    secret_key = '6LdpX4QaAAAAAOtH3ttoY9i7jnRxcP6tTflBJqvu'

    data = {'secret': secret_key, 'response': token}
    r = requests.get(verify_url, data)
    response = r.json()

    if response['success']:
        redirect_url = url_for('data')
        return redirect_url
    else:
        return 'NOK'
