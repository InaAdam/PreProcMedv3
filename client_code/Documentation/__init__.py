from ._anvil_designer import DocumentationTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Documentation(DocumentationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.layout.home_nav_btn.visible = True
    self.layout.doc_nav_btn.visible = False
    # Any code you write here will run before the form opens.

  def button_dwnld_ipynb_click(self, **event_args):
    file  = anvil.server.call('get_file')
    anvil.media.download(file)

  def link_user_profile_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('User')

  def link_itk_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
    
