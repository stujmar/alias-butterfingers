import os
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if "add" in sys.argv:
  print("Adding")
  git_add_all = "git add ."
  os.system(git_add_all)

if "commit" in sys.argv:
  print("Commiting")
  git_commit = "git commit -m '" + sys.argv[2] + "'"
  os.system(git_commit)

