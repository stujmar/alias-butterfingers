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

# python alias.py add message "your commit message here" push

# git commit --date='2022-02-08 12:12:45 -m 'test commit message'
# GIT_COMMITTER_DATE="Tues Feb 8 14:00 2022 +0100" git commit --amend --no-edit
