from wtforms.fields import Field, FieldList as WtfFieldList

class FieldWithScript(Field):
    """
    An abstract class that represents a field that comes with some javascript.

    :param script - the script to store in self.script
    """

    def __init__(self, script, label=u'', validators=None, filters=tuple(), description=u'', id=None, default=None,
                 widget=None, _form=None, _name=None, _prefix='', _translations=None):
        self.script = script
        super(FieldWithScript, self).__init__(label, validators, filters, description, id, default, widget, _form,
                                              _name, _prefix, _translations)