import os


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


def get_changed_files(repo):
    for item in repo.index.diff(None):
        print(item.a_path)


def get_status(repo, path):
    changed = [ item.a_path for item in repo.index.diff(None) ]
    if path in repo.untracked_files:
        return 'untracked'
    elif path in changed:
        return 'modified'
    else:
        return 'deleted'