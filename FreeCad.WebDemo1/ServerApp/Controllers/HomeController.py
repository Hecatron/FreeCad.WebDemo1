from ServerApp.FlaskServer import flaskserv
from flask import render_template
app = flaskserv.app


@app.route('/')
def home():
    return render_template(
        'home.html',
        title='FreeCad.WebDemo1 - Home'
    )
