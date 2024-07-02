from ._anvil_designer import VisualTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Visual(VisualTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.layout.visual_btn_menu.role = self.layout.btn_menu_active
    if properties['path']:
      self.text_box_path.text =properties['path']
    self.button_itk.enabled = anvil.server.call('btn_app_active','itk_path')
    self.button_microdcm.enabled = anvil.server.call('btn_app_active','microdicom_path')
    self.button_tdslicer.enabled = anvil.server.call('btn_app_active','tdslicer_path')

    if any(elem in properties for elem in ['params','paths_set']):
      self.button_back.enabled = True
      self.item['paths_set'] = properties['paths_set']
      self.item['params'] = properties['params']

  def button_itk_click(self, **event_args):
    anvil.server.call('open_application',self.text_box_path.text,'itk')

  def button_microdcm_click(self, **event_args):
    anvil.server.call('open_application',self.text_box_path.text,'mdicom')

  def button_tdslicer_click(self, **event_args):
    anvil.server.call('open_application',self.text_box_path.text,'tdslicer')

  def button_back_click(self, **event_args):
    open_form('Home_pkg.Anonym',paths_set = self.item['paths_set'],
             params = self.item['params'])
