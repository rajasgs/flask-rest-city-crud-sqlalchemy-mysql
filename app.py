'''
    Source:

    https://pypi.org/project/python-dotenv/
'''

from flask import Flask
from rest_api import *
import os
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

app.register_blueprint(api)



'''
@app.route("/")
def hello():
    return "Hello World!"
'''


@app.route("/env")
def get_env():

    postgres_uri = os.getenv("POSTGRES_URI")

    return postgres_uri


if __name__ == "__main__":
    
    app.config['city'] = 'Toronto'
    
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)