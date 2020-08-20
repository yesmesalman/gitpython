from git import Repo
import gitpython_script.env as env
import gitpython_script.index as func
import sys

repo = Repo(env.REPO_DIR)


if func.check_repository(repo) == False:
    print("repo doesn't exists.")
    sys.exit()


print("repo '"+ func.get_repository_name(repo) +"' added \n")


func.get_changed_files(repo)



sys.exit()