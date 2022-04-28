from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page!</h1>
            <p>This is the Home page!</p>
            <a href='/welcome'>Go to the Welcome Page</a><br>
            <a href='/welcome/home'>Go to the Welcome Home Page</a><br>
            <a href='/welcome/back'>Go to the Welcome Back Page</a><br>
        <body>
    </html>
    
    """
    return html

@app.route('/welcome')
def welcome_page():
    html = """
    <html>
        <body>
            <h1>Welcome Page!</h1>
            <p>This is the Welcome page!</p>
            <a href='/welcome/home'>Go to the Welcome Home Page</a><br>
            <a href='/welcome/back'>Go to the Welcome Back Page</a><br>
            <a href='/'>Go to the Home Page</a><br>
        <body>
    </html>
    
    """
    return "welcome"

@app.route('/welcome/home')
def welcome_home_page():
    html = """
    <html>
        <body>
            <h1>Welcome Home Page!</h1>
            <p>This is the Welcome Home page!</p>
            <a href='/welcome/back'>Go to the Welcome Back Page</a><br>
            <a href='/'>Go to the Home Page</a><br>
        <body>
    </html>
    
    """
    return "welcome home"

@app.route('/welcome/back')
def welcome_back_page():
    html = """
    <html>
        <body>
            <h1>Welcome Back Page!</h1>
            <p>This is the Welcome Back page!</p>
            <a href='/welcome/home'>Go to the Welcome Home Page</a><br>
            <a href='/'>Go to the Home Page</a><br>
        <body>
    </html>
    
    """
    return "welcome back"