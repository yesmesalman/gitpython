import os
import gitpython_script.env as env
from ftplib import error_perm


def check_repository(repo):
    try:
        repo.git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False

def get_repository_name(repo):
    remote_url = repo.remotes[0].config_reader.get("url")
    repo_name = os.path.splitext(os.path.basename(remote_url))[0]
    return repo_name


def print_changed_files(repo):
    for item in repo.index.diff(None):
        print(get_status(repo, item.a_path)+': '+item.a_path)


def get_changed_files(repo):
    return [ get_file_directory(item.a_path) for item in repo.index.diff(None) ]


def get_status(repo, path):
    changed = [ item.a_path for item in repo.index.diff(None) ]
    if path in repo.untracked_files:
        return 'untracked'
    elif path in changed:
        return 'modified'
    else:
        return 'deleted'


def get_file_directory(filename):
    arr = filename.split('/')
    dir = '/'

    if(len(arr) != 1):
        dir = ''
        for d in arr[:-1]:
            dir += d+"/"
        
    return [arr[(len(arr) - 1)], dir]

def createDirs(ftp, dirpath):
    dirpath = dirpath.replace('\\', '/')
    tmp = dirpath.split('/')
    dirs = []

    for _ in tmp:
        if len(dirs) == 0:
            dirs.append(_)
            continue

        dirs.append(dirs[-1] + '/' + _)

    for _ in dirs:
        try:
            ftp.mkd(_)
        except error_perm as e:
            e_str = str(e)
            
            if '550' in e_str and 'File exists' in e_str:
                continue


def upload_file(ftp, file):
    try:
        createDirs(ftp, env.REMOTE_SERVER_DIR + file[1])

        file = open(file[0], 'rb')
        ftp.storbinary('STOR '+env.REMOTE_SERVER_DIR + file[0], file)
        file.close()
        print(file[0]+" file uploaded")

    except:
        print("unable to upload file "+file[0])

    
def upload_all_files(ftp, arr):
    for f in arr:
        upload_file(ftp, f)
    