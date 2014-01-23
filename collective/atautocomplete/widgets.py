from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.Widget import LinesWidget
from AccessControl import ClassSecurityInfo

class LinesAutoCompleteWidget(LinesWidget):

    _properties = LinesWidget._properties.copy()
    _properties.update({
        'macro' : "linesautocomplete",
        'helper_js': ('ui.core.min.js','jquery.autocomplete.min.js','linesautocomplete.js'),
        'helper_css' : ('jquery.autocomplete.css',),
        })

    security = ClassSecurityInfo()

    security.declarePublic('process_form')
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """Basic impl for form processing in a widget"""
        value = form.get(field.getName(), empty_marker)
        if value is empty_marker:
            return empty_marker
        if emptyReturnsMarker and value == '':
            return empty_marker
        return [v.strip() for v in value.split(',') if v.strip()!=''], {}

    def isString(self,data):
        if type(data) == str:
           return True
        if type(data) == unicode:
           return True
        return False
    

registerWidget(LinesAutoCompleteWidget,
               title='LinesAutoComplete',
               description=('Renders a HTML textarea for a list '
                            'with autocompleting'),
               used_for=('Products.Archetypes.Field.LinesField',)
               )

