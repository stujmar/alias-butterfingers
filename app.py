import os
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if "add" in sys.argv:
  print("Adding")
  git_add_all = "git add --all"
  os.system(git_add_all)

if "message" in sys.argv:
  print("Commiting")
  git_commit = "git commit -m '" + sys.argv[3] + "'"
  os.system(git_commit)

if "push" in sys.argv:
  print("Pushing")
  git_push = "git push"
  os.system(git_push)


