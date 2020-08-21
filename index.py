from git import Repo
from ftplib import FTP_TLS
import gitpython_script.env as env
import gitpython_script.index as func
import sys

repo = Repo(env.REPO_DIR)

try:
    ftp = FTP_TLS(env.REMOTE_SERVER_HOST)
    ftp.sendcmd('USER '+env.REMOTE_SERVER_USERNAME) # '331 Please specify the password.'
    ftp.sendcmd('PASS '+env.REMOTE_SERVER_PASSWORD)

    # ftp.storbinary('STOR '+env.REMOTE_SERVER_DIR+'index.py', open('gitpython_script/index.py', 'rb'))

except IOError as e:
    print('unable to login with ftp, Please try changing remote FTP credentials.')
    sys.exit()


if func.check_repository(repo) == False:
    print("repo doesn't exists.")
    sys.exit()


print("repo '"+ func.get_repository_name(repo) +"' added \n")
print(func.get_changed_files(repo))



# sys.exit()