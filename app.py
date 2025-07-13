from flask import Flask, redirect, render_template, session, url_for, jsonify
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Check required environment variables
required_env = ['FLASK_SECRET_KEY', 'AUTH0_CLIENT_ID', 'AUTH0_CLIENT_SECRET', 'AUTH0_DOMAIN']
for var in required_env:
    if not os.getenv(var):
        print(f"Error: Environment variable {var} is missing.")
        sys.exit(1)

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']

oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=os.environ['AUTH0_CLIENT_ID'],
    client_secret=os.environ['AUTH0_CLIENT_SECRET'],
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url=f"https://{os.environ['AUTH0_DOMAIN']}/.well-known/openid-configuration"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=url_for('callback', _external=True))

@app.route('/callback')
def callback():
    token = auth0.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/dashboard')

# @app.route('/dashboard')
# def dashboard():
#     user = session.get('user')
#     if not user:
#         return redirect('/')
#     return jsonify(user)

@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect('/')
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(
        f"https://{os.environ['AUTH0_DOMAIN']}/v2/logout?returnTo={url_for('home', _external=True)}&client_id={os.environ['AUTH0_CLIENT_ID']}"
    )

if __name__ == '__main__':
    app.run(debug=True)
