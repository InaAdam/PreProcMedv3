from ._anvil_designer import UserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class User(UserTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_user_email.text = anvil.server.call('user_table_use',['get'],'email')
    self.text_box_itk_path.text = anvil.server.call('user_table_use',['get'],'itk_path')
    self.text_box_mdicom_path.text = anvil.server.call('user_table_use',['get'],'microdicom_path')
    self.text_box_tdslicer_path.text = anvil.server.call('user_table_use',['get'],'tdslicer_path')

  def button_select_itk_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_itk_path.text = "C:\\Program Files\\ITK-SNAP 4.0\\bin\\ITK-SNAP.exe"

  def button_update_itk_click(self, **event_args):
    anvil.server.call('user_table_use',['write',self.text_box_itk_path.text],'itk_path')
    alert('ITK-Snap local location succesfully updates')
    self.button_update_itk.enabled = False

  def button_select_mdicom_click(self, **event_args):
    self.text_box_mdicom_path.text = "C:\\Program Files\\MicroDicom\\mDicom.exe"

  def button_test_mdicom_click(self, **event_args):
    t = anvil.server.call('app_test',self.text_box_mdicom_path.text)
    if t == 0:
      alert('App path invalid')
    elif t == 1:
      self.button_update_mdicom.enabled = True

  def button_update_mdicom_click(self, **event_args):
    anvil.server.call('user_table_use',['write',self.text_box_mdicom_path.text],'microdicom_path')
    alert('MicroDicom local location path succesfully updated')
    self.button_update_mdicom.enabled = False

  def button_change_email_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_pass_reset_click(self, **event_args):
    anvil.users.change_password_with_form(require_old_password=True)

  def button_test_itk_click(self, **event_args):
    """This method is called when the button is clicked"""
    t = anvil.server.call('app_test',self.text_box_itk_path.text)
    if t == 0:
      alert('App path invalid')
    elif t == 1:
      self.button_update_itk.enabled = True

  def button_select_tdslicer_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_tdslicer_path.text = "C:\\Users\\allys\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\Slicer.exe"

  def button_test_tdslicer_click(self, **event_args):
    """This method is called when the button is clicked"""
    t = anvil.server.call('app_test',self.text_box_tdslicer_path.text)
    if t == 0:
      alert('App path invalid')
    elif t == 1:
      self.button_update_tdslicer.enabled = True

  def button_update_tdslicer_click(self, **event_args):
    anvil.server.call('user_table_use',['write',self.text_box_tdslicer_path.text],'tdslicer_path')
    alert('3DSlicer local location path succesfully updated')
    self.button_update_tdslicer.enabled = False
