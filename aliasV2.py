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

# python alias.py add message "your commit message here" push
