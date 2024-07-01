from ._anvil_designer import Dcm2NiiTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Dcm2Nii(Dcm2NiiTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.layout.dcm2nii_btn_menu.role = self.layout.btn_menu_active
    if 'file_path' not in properties:
      #self.item['path'] = "D:\\dicom_anonim\\dicom_test"
      self.button_convert.enabled = False
    else:
      self.text_box_dcm_path.text = properties['file_path']


  def button_open_folder_click(self, **event_args):
    anvil.server.call('open_location',self.item['nii_path'])

  def button_select_click(self, **event_args):
    #self.button_convert.enabled = True
    self.text_box_dcm_path.text = self.item['path']

  def button_convert_click(self, **event_args):
    self.item['nii_path'] = anvil.server.call('nii2dcm',self.text_box_dcm_path.text)
    self.button_open_folder.enabled = True
    self.button_visualize.enabled = True
    alert('Conversion succesfull')

  def text_box_dcm_path_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.button_convert.enabled = True

  def button_visualize_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home_pkg.Visual', path = self.item['nii_path'])
