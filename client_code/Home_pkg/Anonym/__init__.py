from ._anvil_designer import AnonymTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class Anonym(AnonymTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.layout.anonym_btn_menu.role = self.layout.btn_menu_active
    self.drop_down_type.items = ['normal','menisc','ACL','ACL+menisc','artrithis']
    self.drop_down_year.items = anvil.server.call('set_list_years')

    if 'params' in properties:
      self.drop_down_type.selected_value = properties['params'][0]
      self.drop_down_year.selected_value = properties['params'][1]
    if 'paths_set' in properties:
      self.text_box_original_path.text = properties['paths_set'][0]
      self.text_box_anonym_path.text = properties['paths_set'][1]

  def button_anonymize_click(self, **event_args):
    self.button_anonymize.enabled = False
    if not self.text_box_original_path.text:
      alert("Original data path empty")
      return
    if not self.text_box_anonym_path.text:
      alert("Anonym path empty")
      return
    path_original = self.text_box_original_path.text
    path_anonym = self.text_box_anonym_path.text
    type = self.drop_down_type.selected_value
    year = self.drop_down_year.selected_value
    tp = anvil.server.call('anonym',path_original,path_anonym,type,year)
    if tp == 0:
      alert('The selected directory doesn\'t contain any dicom series')
      return
    self.label_track.visible = True
    if tp[0] == 'single':
      self.label_track.text = f'''One dicom series was detected.\n
                              Successfuly anonymized and saved in:\n{tp[1]}'''
    if tp[0] == 'multiple':
      self.label_track.text = f'''Multiple dicom series were detected.\n
                              Background process started. Data will be saved in:\n{tp[1]}'''
    self.item['pass_path'] = tp[1]
    self.button_file_location.enabled = True
    self.button_visual.enabled = True
    self.button_dcm2nii.enabled = True

  def button_visual_click(self, **event_args):
    open_form('Home_pkg.Visual',path = self.item['pass_path'],
             paths_set = [self.text_box_original_path.text,self.text_box_anonym_path.text],
             params = [self.drop_down_type.selected_value,self.drop_down_year.selected_value,
                      self.radio_button_pd.get_group_value(),self.radio_button_sagittal.get_group_value()])

  def text_box_original_path_change(self, **event_args):
    self.button_anonymize.enabled = True

  def text_box_anonym_path_change(self, **event_args):
    self.button_anonymize.enabled = True

  def button_file_location_click(self, **event_args):
    anvil.server.call('open_location',self.item['pass_path'])

  def button_dcm2nii_click(self, **event_args):
    open_form('Home_pkg.Dcm2Nii', file_path = self.item['pass_path'],
             paths_set = [self.text_box_original_path.text,self.text_box_anonym_path.text],
             params = [self.drop_down_type.selected_value,self.drop_down_year.selected_value,
                      self.radio_button_pd.get_group_value(),self.radio_button_sagittal.get_group_value()])
    
