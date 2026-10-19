from find_file_lib import find_file_certain_date
from datetime import datetime

today = datetime.today()
result = find_file_certain_date(
    folder="/Users/kirstenliu/python/randall_toolkits/find_file_ver/tests/Blend Cards", 
    date_format="%Y%m%d", 
    date=today, 
    file_format="%Y%m%d Blend Cards v#.xlsx", 
    last_idx_chop=18
    )
print(result)