from wtforms.fields import Field, FieldList as WtfFieldList

class JqField(Field):
    """
    An abstract class that represents a field that comes with some javascript.

    :param script - the script to store in self.script
    """

    def __init__(self, label=u'', validators=None, filters=tuple(), description=u'', id=None, default=None,
                 widget=None, script=None, _form=None, _name=None, _prefix='', _translations=None):
        self._script = script
        super(JqField, self).__init__(label, validators, filters, description, id, default, widget, _form,
                                              _name, _prefix, _translations)

    def render_script(self):
        if self._script is not None:
            return "<script type='language/javascript'>%s</script>" % self._script
        else:
            return ""

    @property
    def script(self):
        """
        A method for explicit calling script (for example into head). If not called,
        the script is to be rendered just before the field.
        """
        self.script_called = True
        return self.render_script()

