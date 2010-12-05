from wtforms.ext.jquery.widgets import JqTableWidget
from wtforms.ext.jquery.fields import JqFormField
from unittest import TestCase
from wtforms.form import Form
from wtforms.fields import TextField

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
                                                 '<tr><th>lfoo</th><td>foo</td><td><a href="#">x</a></td></tr>' +
                                                 '<tr><th>lbar</th><td>bar</td><td><a href="#">x</a></td></tr>' +
                                                 '</table>')

        self.assertEqual(JqTableWidget(delete_row_link=False)(field), u'<table id="hai">' +
                                                                       '<tr><th>lfoo</th><td>foo</td></tr>' +
                                                                       '<tr><th>lbar</th><td>bar</td></tr>' +
                                                                       '</table>')
class JqFormFieldTest(TestCase):

    def setUp(self):
        F = make_form(
            a = TextField(),
            b = TextField(),
        )
        self.F1 = make_form('F1', a = JqFormField(F))
        self.F2 = make_form('F2', a = JqFormField(F, separator='::'))

    def test_script(self):
        form = self.F1(DummyPostData({'a-a':[u'moo']}))
        print form.__dict__