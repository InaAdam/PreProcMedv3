import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

def open_itk(path):
  itk_app_link = anvil.server.call('user_table_use',['get'],'itk_path')
  dcms = anvil.server.call('access_path',[path],['directory_list'])
  anvil.server.call('access_path',[path+"\\"+dcms[0]],['open_file_in_app',itk_app_link])

def open_mdicom(path):
  mdicom_app_link = anvil.server.call('user_table_use',['get'],'microdicom_path')
  anvil.server.call('access_path',[path],['open_file_in_app',mdicom_app_link])

def open_tdslicer(path):
  tdslicer_app_link =  anvil.server.call('user_table_use',['get'],'tdslicer_path')
  anvil.server.call('access_path',[path],['open_file_in_app',tdslicer_app_link])

@anvil.server.callable
def open_application(path, app):
  match app:
    case 'itk':
      open_itk(path)
    case 'mdicom':
      open_mdicom(path)
    case 'tdslicer':
      open_tdslicer(path)

@anvil.server.callable
def btn_app_active(app):
  current_user = anvil.users.get_user()['email']
  user_row = app_tables.users.get(email=current_user)
  print(user_row[app])
  if user_row[app]:
    return True
  else:
    return False


@anvil.server.callable
def open_location(path):
  anvil.server.call('access_path',[path],['open_location'])