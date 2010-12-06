from wtforms.fields import Field, FieldList
from wtforms.ext.jquery import widgets

class JqField(Field):
    """
    An abstract class that represents a field that comes with some javascript.
    """
    _script = ''
    _script_called = False

    def get_script(self):
        return self._script

    def render_script(self, script=None):
        script_to_render = script or self.get_script()
        if script_to_render is not None:
            return "<script type='text/javascript'>%s</script>" % script_to_render
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

    def __init__(self, unbound_field, label=u'', validators=None, min_entries=0, max_entries=None, default=tuple(),
                 widget=widgets.JqTableWidget(), **kwargs):
        self.widget = widget
        super(JqFieldTable, self).__init__(unbound_field, label, validators, min_entries, max_entries, default,
                                           **kwargs)

    def get_delete_item_class(self):
        if self.widget is None:
            return None
        else:
            return getattr(self.widget, 'delete_item_link_class', None)

    def get_script(self):
        delete_item_class = self.get_delete_item_class()
        if delete_item_class is None:
            return ''
        else:
            return  ("(function($){$(document).ready("+\
                    "function(){$('.%s').live('click',function(e){$(e.target).closest('tr').remove()})})})"+\
                    "(jQuery);") % delete_item_class
        


