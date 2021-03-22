from flask import Flask, render_template, request, url_for
import requests
import json
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/captcha')
def captcha():
    id = request.args.get('id', None)

    if id is not None:
        data = ''
        return render_template('captcha.html', data=data)
    else:
        return render_template('error.html')

# @app.route('/data')
# def data():
#     return render_template('data.html')

@app.route('/verify', methods=['POST'])
def verify():
    data = json.loads(request.data)

    if data['token']:
        token = data['token']
    else:
        return render_template('captcha.html')

    if data['id']:
        id = data['id']
    else:
        return render_template('captcha.html')
    
    # FIXME: should be in yaml files
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    secret_key = '6LdpX4QaAAAAAOtH3ttoY9i7jnRxcP6tTflBJqvu'

    data = {'secret': secret_key, 'response': token}
    r = requests.get(verify_url, data)
    response = r.json()

    if response['success']:
        data['id'] = id
        data['value'] = 'donnée'
        # redirect_url = url_for('data')
        return render_template('captcha.html', data=data)
    else:
        return render_template('captcha.html')
