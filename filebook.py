import shutil
import datetime
def sadres():
   now = datetime.datetime.now().time()
   str1 = 'work/adress/'
   str2 = str(now)
   str2 = str2.replace('.',"_")
   str2 = str2.replace(':',"_")
   str3 = '.xlsx'
   strend = (str1  + str2 + str3)
   shutil.copy('template/adress_template.xlsx', strend)
   return strend

