from wtforms.fields import Field, FieldList
from wtforms.ext.jquery import widgets

class JqField(Field):
    """
    An abstract class that represents a field that comes with some javascript.
    """
    _script = ''
    _script_called = False

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
        if not self._script_called:
            self._script_called = True
            return self.render_script()
        else:
            return ''

    def __call__(self, **kwargs):
        return "%s%s" % (self.script, super(JqField, self).__call__(**kwargs),)

class JqFieldTable(JqField, FieldList):
    #TODO: some code that deletes some items
    _script = ""
    widget=widgets.JqTableWidget()
