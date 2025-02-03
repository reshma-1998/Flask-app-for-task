from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to Flask."

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password':  # Example credentials check
            return redirect(url_for('home'))
        return "Invalid credentials, please try again."
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Sign In">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
