from flask import Blueprint,render_template,session

home_bp = Blueprint('home',__name__)


@home_bp.route('/')
def home():
    if 'user' in session:
        return render_template('index.html',username = session['user'])
    else:
        return render_template('login.html')