import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import datetime
import os


@anvil.server.callable
def set_list_years():
  currentDateTime = datetime.datetime.now()
  current_date = currentDateTime.date()
  current_year = current_date.year
  initial_year = 1950
  year_list = [str(i).zfill(4) for i in range(current_year,initial_year+1, -1)]
  return year_list


def get_pacient_folder(path_data):
  path_verify = anvil.server.call('access_path',[path_data+'\\**\\'+'*.dcm'],['search'])
  if path_verify == 0:
    print("no dicom series in current directory")
    return 0
  pacient_folder = anvil.server.call('access_path',[path_verify],['get_root_dir',"../../.."])
  if pacient_folder == path_data:
    return ['single',pacient_folder]
  else:
    pacients_folders = anvil.server.call('access_path',[pacient_folder],['get_root_dir',".."])
    return ['multiple',pacients_folders]

def anonym_dcm(dcm_serie, folder_anonim,anonim_ppl):
  extra_anonymization_rules = {}
  idx = 1
  try:
    dcm_files = anvil.server.call('access_path',[dcm_serie],['directory_list'])
    for dcm in dcm_files:
      anvil.server.call('access_path',[dcm_serie+'\\'+dcm,folder_anonim],['dcm_anonim',extra_anonymization_rules])
      anvil.server.call('access_path',[folder_anonim+'\\'+dcm,folder_anonim+'\\'+anonim_ppl+'_'+str("{:02d}".format(idx))+'.dcm'],['rename'])
      idx=idx+1
  except:
    return "not found"
@anvil.server.callable
def anonym(origin_path,anonym_path,type,year):
  pacient_folder = get_pacient_folder(origin_path)
  if pacient_folder == 0:
    return 0
  time_now = f'{datetime.datetime.now():%Y_%m_%d-%H_%M_%S%z}'
  headrs = [['Time','Original data path','Anonym data path']]
  csv_name = origin_path+"\\"+time_now+".csv"
  anvil.server.call('access_path',[csv_name],['write_csv',headrs])
  if pacient_folder[0] == 'single':
    dcm_serie = anvil.server.call('access_path',[pacient_folder[1]+'\\**\\'+'*_pd_tse_fs_[SAG][sag]*'],['search'])
    patient_anonym = 'P'+type[0]+year
    pat_anonym_path = anonym_path+'\\'+time_now+'\\'+type+'\\'+patient_anonym+'\\'+'dicom'
    anvil.server.call('access_path',[pat_anonym_path],['create'])
    anonym_dcm(dcm_serie,pat_anonym_path,patient_anonym)
    csv_data = [[time_now,dcm_serie,pat_anonym_path]]
    anvil.server.call('access_path',[csv_name],['write_csv',csv_data])
    return [pacient_folder[0],pat_anonym_path]
  elif pacient_folder[0] == 'multiple':
    pacient_list = anvil.server.call('access_path',[pacient_folder[1]],['directory_list'])
    anvil.server.launch_background_task('multiple_anonym',pacient_list,pacient_folder,anonym_path,time_now,year,type,csv_name)
    return [pacient_folder[0],anonym_path+'\\'+time_now+'\\'+type]
    


@anvil.server.background_task
def multiple_anonym(pacient_list,pacient_folder,anonym_path,time_now,year,type,csv_name):
    idx = 1
    pacient_list = [p for p in pacient_list if ".csv" not in p]
    for pacient in pacient_list:
      dcm_serie = anvil.server.call('access_path',[pacient_folder[1]+'\\'+pacient+'\\**\\'+'*_pd_tse_fs_[SAG][sag]*'],['search'])
      patient_anonym = 'P'+str(idx)+type[0]+year
      print(f"Pacient {idx}/{len(pacient_list)}")
      #pat_anonym_path = anonym_path+'\\'+time_now+'\\'+type+'\\'+patient_anonym+'\\'+'dicom'
      pat_anonym_path = anonym_path+'\\'+type+'\\'+patient_anonym+'\\'+'dicom'
      a = anvil.server.call('access_path',[pat_anonym_path],['create'])
      if a == "not found":
        csv_data = [[time_now,pacient,"no relevant data found"]]
        anvil.server.call('access_path',[csv_name],['write_csv',csv_data])
      else:
        anonym_dcm(dcm_serie,pat_anonym_path,patient_anonym)
        csv_data = [[time_now,dcm_serie,pat_anonym_path]]
        anvil.server.call('access_path',[csv_name],['write_csv',csv_data])
        idx = idx+1