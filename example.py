try:
  from pytools.organize import CodeOrganizer
except:
  import os
  os.system("pip install Pytools.api")



file_path = "your/path/to/file.py"
organizer = CodeOrganizer()
organizer.organize_code_file(file_path)
