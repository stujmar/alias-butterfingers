import os
import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

# if "add" in sys.argv:
#   print("Adding")
#   git_add_all = "git add --all"
#   os.system(git_add_all)

# if "message" in sys.argv:
#   print("Commiting")
#   git_commit = 'git commit -m "' + str(sys.argv[3]) + '"'
#   print('commit:', git_commit)
#   os.system(git_commit)

# if "push" in sys.argv:
#   print("Pushing")
#   git_push = "git push"
#   os.system(git_push)

stage_unstage = "git add . && git reset"
os.system(stage_unstage)

stage = "git add ."
os.system(stage)
commit = 'git commit -m "' + str(sys.argv[0]) + '"'
os.system(commit)
push = "git push"
os.system(push)

# Try running the following command in the terminal
# python commit.py "your commit message here"

# git commit --date='2022-02-22 12:12:45 -m 'test commit message'
# git commit --amend --date="2022-02-22 16:55:55"
# GIT_COMMITTER_DATE="Tues Feb 22 14:00 2022 +0100" git commit --amend --no-edit
