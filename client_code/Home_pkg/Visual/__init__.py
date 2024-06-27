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

  def button_itk_click(self, **event_args):
    anvil.server.call('open_application',self.text_box_path.text,'itk')

  def button_microdcm_click(self, **event_args):
    anvil.server.call('open_application',self.text_box_path.text,'mdicom')

  def button_path_click(self, **event_args):
    self.text_box_path.text = "D:\\dicom_anonim\\anonim_test\\2024_06_14-14_25_47\\normal\\Pn2024\\dicom"

  def button_tdslicer_click(self, **event_args):
    anvil.server.call('open_application',self.text_box_path.text,'tdslicer')
