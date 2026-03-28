from flask import Blueprint,render_template, request,session,flash,redirect,url_for

from werkzeug.security import generate_password_hash,check_password_hash
login_bp =Blueprint('login',__name__)


users = {
    "alice": generate_password_hash('alice123'),
    "bob" : generate_password_hash('bob123')
}
@login_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and check_password_hash(users[username],password):
            session['user']=username
            return redirect(url_for('home.home'))
        else:
            flash('Invalid Password')
            return redirect(url_for('login.login'))
    
    return render_template('login.html')
    
@login_bp.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login.login'))