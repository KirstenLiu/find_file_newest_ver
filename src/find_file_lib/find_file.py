from datetime import datetime
from pathlib import Path
from fnmatch import fnmatch

def find_file_certain_date(folder: str, date_format: str, date: datetime, file_format: str, last_idx_chop: int) -> str:
    #i.e. file_format = '%Y%m%d Blend Cards v#.xlsx'
    
    #i.e. "%Y%m%d"
    date_str = date.strftime(date_format)
    pattern = file_format.replace(date_format, date_str).replace("#", "*")
    print("pattern: ", pattern)

    folder = Path(folder)
    max_ver = -1
    max_ver_file = ""

    for path in folder.rglob("*"):
        if path.is_file:
            file_name = path.name
            print(file_name, file_format[:last_idx_chop])
            if fnmatch(file_name, pattern):
                v_idx = file_name.find('v')
                if v_idx + 1 < len(file_name):
                    ver = int(file_name[v_idx+1])
                    if ver > max_ver:
                        max_ver = ver
                        max_ver_file = file_name
                elif v_idx == -1 and len(max_ver_file)==0:
                    max_ver_file = pattern[:last_idx_chop]+".xlsx"
            elif fnmatch(file_name, file_format[:last_idx_chop].replace(date_format, date_str)+"*") and len(max_ver_file)==0:
                max_ver_file = file_name
    print("max_ver_file: ", max_ver_file)
    return max_ver_file

def find_file_historically():
    return
