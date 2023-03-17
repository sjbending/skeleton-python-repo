import sys
import subprocess

author_name = str(subprocess.check_output(["git", "config", "--get", "user.name"]))
author_email = str(subprocess.check_output(["git", "config", "--get", "user.email"]))
author_name = author_name.strip("b'")
author_email = author_email.strip("b'")

# NOTE: Slicing only way I could remove the persistent "\n" at the end of the strings
if (author_name[:len(author_name) - 2] == "" or author_email[:len(author_name) - 2] == ""):
    print("ERROR: could not acquire valid user.name and user.email from your git config.")
    sys.exit(1)

include_cuda = "{{ cookiecutter.include_cuda }}"

if include_cuda != "y" and include_cuda != "n":
    print('ERROR: include_cuda must be either "y" or "n", not %s.' % include_cuda)
    sys.exit(1)

