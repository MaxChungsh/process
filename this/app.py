from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


from routes import *

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)