from flask import Flask
from wtforms.form import Form
from wtforms.ext.jquery.fields import JqFieldTable
from wtforms.fields import FormField, TextField

app = Flask(__name__)

class IMForm(Form):
    protocol = TextField()
    username = TextField()

class ContactForm(Form):
    first_name  = TextField()
    last_name   = TextField()
    im_accounts = JqFieldTable(FormField(IMForm))

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()