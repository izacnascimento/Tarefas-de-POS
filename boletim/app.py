from flask import Flask, redirect, url_for, session, request, render_template
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_secret_key')

# Configurações do OAuth2
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
AUTHORIZATION_BASE_URL = 'https://suap.ifrn.edu.br/oauth2/authorize/'
TOKEN_URL = 'https://suap.ifrn.edu.br/oauth2/token/'
API_BASE_URL = 'https://suap.ifrn.edu.br/api/'

def get_oauth_session(token=None):
    return OAuth2Session(CLIENT_ID, token=token, redirect_uri=url_for('callback', _external=True))

@app.route('/')
def index():
    if 'oauth_token' in session:
        return redirect(url_for('user_profile'))
    return render_template('index.html')

@app.route('/login')
def login():
    oauth = get_oauth_session()
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    oauth = get_oauth_session()
    token = oauth.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)
    session['oauth_token'] = token
    return redirect(url_for('user_profile'))

@app.route('/user_profile')
def user_profile():
    if 'oauth_token' not in session:
        return redirect(url_for('index'))
    oauth = get_oauth_session(session['oauth_token'])
    user_info = oauth.get(f'{API_BASE_URL}v2/minhas-informacoes/').json()
    return render_template('user.html', user_info=user_info)

@app.route('/boletim')
def boletim():
    if 'oauth_token' not in session:
        return redirect(url_for('index'))
    ano_letivo = request.args.get('ano', '2024')
    periodo_letivo = request.args.get('periodo', '1')
    oauth = get_oauth_session(session['oauth_token'])
    url = f'{API_BASE_URL}v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/'
    response = oauth.get(url)
    if response.status_code == 200:
        boletim_data = response.json()
        return render_template('boletim.html', boletim=boletim_data)
    return f"Erro ao obter boletim: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
