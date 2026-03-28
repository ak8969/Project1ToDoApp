from flask import Flask
from routes.login import login_bp
from routes.home import home_bp
from dotenv import load_dotenv
import os


load_dotenv()



app = Flask(__name__)
app.secret_key = os.getenv("MY_SECRET_KEY")

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)

if __name__=='__main__':
    app.run(debug=True)
