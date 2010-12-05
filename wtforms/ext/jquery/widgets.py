from wtforms.widgets import TableWidget, ListWidget

"""
function add_photo() {
      $('<div class="photo_box"><input name="photo" type="file" /></div>').append(
        $('<a href="#">удалить</a>').css({ marginLeft: '5px', fontSize: '11px' }).click( function() {
          $(this).parent().remove();
          return false;
        } )
      ).appendTo('#add_photo');
      return false;
    }
"""

class JqListWidget(ListWidget):
    pass

class JqTableWidget(TableWidget):
    pass