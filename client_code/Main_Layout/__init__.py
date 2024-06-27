from ._anvil_designer import Main_LayoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Main_Layout(Main_LayoutTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def home_nav_btn_click(self, **event_args):
    open_form('Home_pkg.Home')

  def doc_nav_btn_click(self, **event_args):
    open_form('Documentation')

  def user_nav_btn_click(self, **event_args):
    open_form('User')


