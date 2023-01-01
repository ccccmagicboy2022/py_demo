#!d:\cccc2020\TOOL\python-3.9.1-embed-win32\python.exe

from git import Repo
import os

def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))

def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name,
                                     commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(),
                                              commit.size)))

local_path = os.getcwd()
repo = Repo(local_path)

branch_list = repo.remote().refs
print(branch_list)

if repo.is_dirty():
    print(repo.untracked_files)

print_repository(repo)
commits = list(repo.iter_commits('bfsk_acm32'))[:5]

for commit in commits:
    print_commit(commit)
    pass


