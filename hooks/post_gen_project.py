import os
import shutil
import subprocess


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

# Manually replace author name and email from git config
author_name = str(subprocess.check_output(["git", "config", "--get", "user.name"]))
author_email = str(subprocess.check_output(["git", "config", "--get", "user.email"]))
author_name = author_name.strip("b'")
author_email = author_email.strip("b'")


def replace_author_and_email(filename: str):
    with open(filename, 'r') as f:
        # NOTE: Slicing only way I could remove the persistent "\n" at the end of the strings
        dictionary = {
            "[ AUTHOR_NAME ]": author_name[:len(author_name) - 2],
            "[ AUTHOR_EMAIL ]": author_email[:len(author_email) - 2]
        }
        s = f.read()
        for key in dictionary.keys():
            s = s.replace(key, dictionary[key], 1)

    with open(filename, 'w') as f:
        f.write(s)


replace_author_and_email("{{ cookiecutter.__project_slug }}/__init__.py")
replace_author_and_email("pyproject.toml")

subprocess.call(['git', 'init', '-b', 'main'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# Check whether devcontainer CLI is installed
if shutil.which("devcontainer"):
    print("Open {{ cookiecutter.project_name }} in devcontainer?")
    openval = input("[y/n?]: ")
    if openval == "y":
        subprocess.call(['devcontainer', 'open'])
