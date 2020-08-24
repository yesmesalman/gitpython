from git import Repo
from ftplib import FTP
import gitpython_script.env as env
import gitpython_script.index as func
import sys
repo = Repo(env.REPO_DIR)


# FTP Connection
try:
    ftp = FTP(env.REMOTE_SERVER_HOST, env.REMOTE_SERVER_USERNAME, env.REMOTE_SERVER_PASSWORD)

except IOError as e:
    print('unable to login with ftp, Please try changing remote FTP credentials.')
    sys.exit()

# Repo
if func.check_repository(repo) == False:
    print("repo doesn't exists.")
    sys.exit()

print("repo '"+ func.get_repository_name(repo) +"' added \n")


# Upload changed files
func.upload_all_files(ftp, func.get_changed_files(repo))


# End
sys.exit()