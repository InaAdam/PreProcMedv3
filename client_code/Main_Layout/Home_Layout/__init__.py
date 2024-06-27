from ._anvil_designer import Home_LayoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Home_Layout(Home_LayoutTemplate):
  def __init__(self, **properties):
    self.layout.home_nav_btn.visible = False
    self.layout.doc_nav_btn.visible = True
    self.init_components(**properties)
  
  def home_btn_menu_click(self, **event_args):
    open_form('Home_pkg.Home')

  def anonym_btn_menu_click(self, **event_args):
    open_form('Home_pkg.Anonym')

  def dcm2nii_btn_menu_click(self, **event_args):
    open_form('Home_pkg.Dcm2Nii')

  def visual_btn_menu_click(self, **event_args):
    open_form('Home_pkg.Visual',path='')

  def todo_btn_menu_click(self, **event_args):
    open_form('Home_pkg.ToDo')
