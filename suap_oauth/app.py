from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'development'
oauth = OAuth(app)

# Configuração do OAuth
oauth.register(
    name='suap',
    client_id="seu-client-id",
    client_secret="seu-client-secret",
    api_base_url='https://suap.ifrn.edu.br/api/',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
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

@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    if token:
        session['suap_token'] = token
        return redirect(url_for('boletim'))
    return redirect(url_for('index'))

@app.route('/boletim', methods=['GET', 'POST'])
def boletim():
    if 'suap_token' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        ano_letivo = request.form['ano_letivo']
        periodo_letivo = request.form['periodo_letivo']
        api_url = 'https://suap.ifrn.edu.br/api/'
        cabecalhos = {"Authorization": f'Bearer {session["suap_token"]["access_token"]}'}

        boletim_data = obter_boletim(api_url, cabecalhos, ano_letivo, periodo_letivo)

        if boletim_data == "INVALID_TOKEN":
            return redirect(url_for('login'))
        
        return render_template('boletim.html', boletim=boletim_data)
    
    return render_template('boletim.html', boletim=None)

if __name__ == '__main__':
    app.run(debug=True)

def obter_dados_boletim(token, ano_letivo, periodo_letivo):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter boletim: {response.status_code}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
