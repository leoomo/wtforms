from wtforms.ext.jquery.widgets import JqTableWidget
from unittest import TestCase

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

class TableWidgetTest(TestCase):
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
