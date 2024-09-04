from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
import requests

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'  # Alterar para um valor mais seguro em produção
oauth = OAuth(app)

oauth.register(
    name='suap',
    client_id='SEU_CLIENT_ID',  # Substitua pelo seu client_id fornecido pelo SUAP
    client_secret='SEU_CLIENT_SECRET',  # Substitua pelo seu client_secret fornecido pelo SUAP
    api_base_url='https://suap.ifrn.edu.br/api/',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    access_token_method='POST',
    fetch_token=lambda: session.get('suap_token')
)

@app.route('/')
def index():
    if 'suap_token' in session:
        return redirect(url_for('boletim'))
    return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)

@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('boletim'))

@app.route('/boletim')
def boletim():
    if 'suap_token' not in session:
        return redirect(url_for('login'))

    token = session['suap_token']
    ano_letivo = '2024'  # Substitua conforme necessário
    periodo_letivo = '1'  # Substitua conforme necessário

    url = f'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/'
    headers = {
        'Authorization': f'Bearer {token["access_token"]}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        boletim_data = response.json()
        return render_template('boletim.html', boletim=boletim_data)
    else:
        return f"Erro ao obter boletim: {response.status_code}", 500

@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
