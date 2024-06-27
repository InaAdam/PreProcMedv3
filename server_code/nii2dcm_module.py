import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def set_nii_name(op1, op2):
  if op1 == 'dicom':
    nii_name = op2
  else:
    nii_name = op1
  return nii_name

@anvil.server.callable
def nii2dcm(path):
  if path.rsplit('.',1)[-1] == 'dcm':
    nii_name = set_nii_name(path.rsplit("\\",2)[1],path.rsplit("\\",3)[1])
    anvil.server.call('access_path',[path.rsplit("\\",1)[0],path.rsplit("\\",2)[0]],['dcm2nii',nii_name])
  else:
    dcm_list = anvil.server.call('access_path',[path+"\\**\\*.dcm"],['search_all'])
    upper_dcm_list = []
    for dcm in dcm_list:
      if dcm.rsplit('\\',1)[0] not in upper_dcm_list:
        upper_dcm_list.append(dcm.rsplit('\\',1)[0])
    for dir in upper_dcm_list:
      nii_name = set_nii_name(dir.split('\\')[-1],dir.split('\\')[-2])
      anvil.server.call('access_path',[dir,dir.rsplit("\\",1)[0]],['dcm2nii',nii_name])