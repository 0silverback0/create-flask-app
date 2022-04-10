def fill_app_py_file():
    """ creates the boilerplate for app.py """
    app_py_starter_code = ["from flask import Flask, render_template,request, flash, redirect, session\n",
        "from flask_debugtoolbar import DebugToolbarExtension\n",
        "from models import db,connect_db\napp = Flask(__name__)\n",
        "import os\n",
        "app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\n",
        "app.config['SQLALCHEMY_ECHO'] = False\n",
        'app.config["SECRET_KEY"] = "shh"\n',
        "toolbar = DebugToolbarExtension(app)\n",
        "connect_db(app)\n",
        """
        
        \n""",
        "@app.route('/')\n",
        "def home():\n",
        "   return render_template('index.html')"]
    for line in app_py_starter_code:
        with open('app.py', 'a') as f:
            f.write(line)


def fill_templates_index_html():
    """ creates the boilerplate for templates/index.html """
    text = """
    <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title></title>

  <link rel="stylesheet"
        href="https://unpkg.com/bootstrap/dist/css/bootstrap.css">
  <script src="https://unpkg.com/jquery"></script>
  <script src="https://unpkg.com/popper"></script>
  <script src="https://unpkg.com/bootstrap"></script>

  <link rel="stylesheet"
        href="https://use.fontawesome.com/releases/v5.3.1/css/all.css">
  <link rel="stylesheet" href="/static/stylesheets/style.css">
  <link rel="shortcut icon" href="/static/favicon.ico">
</head>

<body>
<h1>Hello From Create Flask App!</h1>
<script src='/static/app.js'></script>
</body>
</html>
    """
    with open('index.html', 'w') as f:
        f.write(text)

def fill_requirements():
    """ fills in the packages for requirements.txt """
    text = """
    bcrypt==3.2.0
    blinker==1.4
    cffi==1.15.0
    click==8.1.2
    Flask==2.1.1
    Flask-Bcrypt==1.0.1
    Flask-DebugToolbar==0.13.1
    Flask-SQLAlchemy==2.5.1
    greenlet==1.1.2
    importlib-metadata==4.11.3
    itsdangerous==2.1.2
    Jinja2==3.1.1
    MarkupSafe==2.1.1
    pycparser==2.21
    python-dotenv==0.20.0
    six==1.16.0
    SQLAlchemy==1.4.35
    Werkzeug==2.1.1
    zipp==3.8.0

    """
    with open('requirements.txt', 'w') as f:
        f.write(text)

def fill_models():
    """ models.py boilerplate template """
    text = ["from flask_bcrypt import Bcrypt\n", "from flask_sqlalchemy import SQLAlchemy\n",
    "bcrypt = Bcrypt()\n", "db = SQLAlchemy()\n", "\nclass Follows(db.Model):\n", "   __tablename__ = 'create-flask-app'\n",
    "   data = db.Column(db.Integer, primary_key=True)", "\ndef connect_db(app):\n", "  db.app = app\n", "  db.init_app(app)"]

    for line in text:
        with open('models.py', 'a') as f:
            f.write(line)