from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Home(HomeTemplate):
  def __init__(self, **properties):
    anvil.users.login_with_form()
    self.init_components(**properties)
    self.layout.home_btn_menu.role = self.layout.btn_menu_active

  def link_documentation_click(self, **event_args):
    open_form('Documentation')
  def link_anonym_click(self, **event_args):
    open_form('Home_pkg.Anonym')
  def link_dcm2nii_click(self, **event_args):
    open_form('Home_pkg.Dcm2Nii')
  def link_visual_click(self, **event_args):
    open_form('Home_pkg.Visual')
