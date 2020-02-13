from git import Repo
import ftplib
repo = Repo('./')


def print_repository(repo):
    # print('Repo description: {}'. format(repo.description))
    print('Active repo branch is {}'. format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))



if not repo.bare:
    # print_repository(repo)
    diff = repo.untracked_files
    print(diff)