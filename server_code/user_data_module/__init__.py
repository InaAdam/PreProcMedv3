import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media

@anvil.server.callable
def get_file():
  myfile = app_tables.local_code.get(file_name = "PreProcMed_App")
  anvil_file = myfile['file']
  return anvil_file

@anvil.server.callable
def app_test(app_path):
  try:
    anvil.server.call('access_path',[''],['open_app',app_path])
    return 1
  except:
    return 0
  
@anvil.server.callable
def user_table_use(operation, column):
  current_user = anvil.users.get_user()['email']
  user_row = app_tables.users.get(email=current_user)
  match operation[0]:
    case 'write':
      user_row[column] = operation[1]
    case 'get':
      return user_row[column]
  