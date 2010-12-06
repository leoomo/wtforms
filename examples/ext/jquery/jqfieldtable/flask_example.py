from flask import Flask, render_template
from wtforms.form import Form
from wtforms.ext.jquery.fields import JqFieldTable
from wtforms.fields import FormField, TextField

app = Flask(__name__)

class DummyPostData(dict):
    def getlist(self, key):
        v = self[key]
        if not isinstance(v, (list, tuple)):
            v = [v]
        return v

class IMForm(Form):
    protocol = TextField()
    uin = TextField()

class ContactForm(Form):
    first_name  = TextField()
    last_name   = TextField()
    im_accounts = JqFieldTable(FormField(IMForm))

class Person(object):
    def __init__(self):
        self.first_name = 'John'
        self.last_name = 'Smith'
        self.im_accounts = [
            {'protocol': 'jabber', 'uin': 'john@example.com'},
            {'protocol': 'email', 'uin': 'john@example.com'}
        ]

@app.route("/")
def index():
    john = Person()
    return render_template('index.html', form=ContactForm(DummyPostData(dict()), john))

if __name__ == "__main__":
    app.run(debug=True)