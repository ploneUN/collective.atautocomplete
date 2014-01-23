collective.atautocomplete
=========================

collective.atautocomplete provide widget using jquery ui auto complete feature. It enable nice web two fields as auto complete multi-select.
It simple offer an alternative for multiselect widget.


requirement:
============

 * Require none

installation:
=============

simply add collective.atautocomplete in your eggs and zcml section in your buildout.cfg and rerun bin/buildout.

using:
======

Example :

from simplejson import dumps as jsondumps
from collective.atautocomplete.widgets import LinesAutoCompleteWidget


        LinesField(
            'multiselectwithautocomplete',
            default='',
            searchable=1,
            default_content_type = 'text/plain',
            allowable_content_types = ('text/plain',),
            vocabularyjsonurl= 'multiselectwithautocompletevocab',
            widget=LinesAutoCompleteWidget(
                label=_(u'label_description', default=u'Description'),
                description=_(u'help_description',
                              default=u'A short summary of the content.'),
                ),
        ),


Browserview for vocab:

from Products.Five.browser import BrowserView
from simplejson import dumps as jsondumps

class MultiSelectWithAutoComplete(BrowserView):
   def __call__(self):
       return jsondumps(['listitem','listitem2'])


zcml:
<browser:page
      for="*"
      name="multiselectwithautocompletevocab"
      permission="zope2.View"
      class=".jsonvocabs.MultiSelectWithAutoComplete"/>

fields:
=======

 * mutliselect : another form of multi select with an textarea and js auto complete

todo:
=====

 * test
 * clean unused js file

history:
========

 * 0.1 : initial release
