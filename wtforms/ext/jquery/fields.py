from wtforms.fields import Field, FieldList
from wtforms.ext.jquery import widgets
from wtforms.form import Form

class JqField(Field):
    """
    An abstract class that represents a field that comes with some javascript.
    """
    _script = None

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
        if not self.script_called:
            self.script_called = True
            return self.render_script()
        else:
            return ''

class JqFormField(JqField, FieldList):
    widget=widgets.TableWidget
