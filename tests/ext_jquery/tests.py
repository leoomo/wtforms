from wtforms.ext.jquery.widgets import JqTableWidget
from wtforms.ext.jquery.fields import JqFieldTable
from unittest import TestCase
from wtforms.form import Form
from wtforms.fields import TextField, FormField

class DummyPostData(dict):
    def getlist(self, key):
        v = self[key]
        if not isinstance(v, (list, tuple)):
            v = [v]
        return v

def make_form(_name='F', **fields):
    return type(_name, (Form, ), fields)

class DummyField(object):
    def __init__(self, data, name='f', label='', id='', type='TextField'):
        self.data = data
        self.name = name
        self.label = label
        self.id = id
        self.type = type

    _value       = lambda x: x.data
    __unicode__  = lambda x: x.data
    __call__     = lambda x, **k: x.data
    __iter__     = lambda x: iter(x.data)
    iter_choices = lambda x: iter(x.data)

class JqTableWidgetTest(TestCase):
    def test(self):
        field = DummyField([DummyField(x, label='l' + x) for x in ['foo', 'bar']], id='hai')
        self.assertEqual(JqTableWidget()(field), u'<table id="hai">' +
                                                 '<tr><th>lfoo</th><td>foo</td><td><a class="delete_row" href="#">x</a></td></tr>' +
                                                 '<tr><th>lbar</th><td>bar</td><td><a class="delete_row" href="#">x</a></td></tr>' +
                                                 '</table>')

        self.assertEqual(JqTableWidget(delete_row_link=False)(field), u'<table id="hai">' +
                                                                       '<tr><th>lfoo</th><td>foo</td></tr>' +
                                                                       '<tr><th>lbar</th><td>bar</td></tr>' +
                                                                   '</table>')

        # testing custom delete link class
        self.assertEqual(JqTableWidget(delete_row_link_class='bzzz')(field), u'<table id="hai">' +
                                                 '<tr><th>lfoo</th><td>foo</td><td><a class="bzzz" href="#">x</a></td></tr>' +
                                                 '<tr><th>lbar</th><td>bar</td><td><a class="bzzz" href="#">x</a></td></tr>' +
                                                 '</table>')


class IMForm(Form):
    protocol = TextField()
    username = TextField()
    
class ContactForm(Form):
    first_name  = TextField()
    last_name   = TextField()
    im_accounts = JqFieldTable(FormField(IMForm))

class JqFieldTableTest(TestCase):
    def setUp(self):
        self.cf = ContactForm(DummyPostData({
                                'first_name': 'John',
                                'last_name': 'Smith',
                                'im_accounts-1-protocol': 'jabber',
                                'im_accounts-1-username': 'example',
                                'im_accounts-2-protocol': 'email',
                                'im_accounts-2-username': 'john@example.com'
                            }))

    def test_remove_links(self):
        self.assertEquals(self.cf.im_accounts().count(u'<td><a class="delete_row" href="#">x</a></td></tr>'), 2)

    def test_script_before_field(self):
        self.assertTrue(self.cf.im_accounts().startswith(u"<script type='language/javascript'>"))

    def test_script_single(self):
        """
        Ensures that script appears only once.
        """
        # first time we callit explicitly and we se it
        self.assertTrue(self.cf.im_accounts.script.startswith(u"<script type='language/javascript'>"))
        # next time we can call it, but we will not se it
        self.assertEquals(self.cf.im_accounts.script, u'')

