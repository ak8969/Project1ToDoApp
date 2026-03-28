from flask import Blueprint,render_template, request

login_bp =Blueprint('login',__name__)

@login_bp.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email,password)
        return render_template('index.html')
    else:
        return render_template('index.html')