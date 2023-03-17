# skeleton-python-repo
Skeleton python repo for use in rapidly setting up new python repositories.

##  Quickstart
Install the latest version of Cookiecutter (must be >= 2.0.0).
```
pip install -U cookiecutter
cookiecutter --version
```

Generate a skeleton python repository in your working directory:
```
cookiecutter git+ssh://git@github.com/sjbending/skeleton-python-repo.git
```
You will be given several prompts for the project name, whether you want to include CUDA libraries, and so on, answer these as appropriate.

## Creating a remote repository and pushing to it
### 1. Using GitHub.com
Head over to the GitHub website and select `Create a new repository`. Fill in the form as appropriate and do not initialise the repository with a `.gitignore`, licenses or a README.

Push your local repository to the repo you just created:
```
git remote add origin git@github.com:<your-github-organisation>/<your-repo-name-here>.git
git push -u origin main
```
###  2. Using Github CLI
To create a remote repository using the github CLI, run:
```
gh repo create
```
Select `create a new repository on GitHub from scratch` and use:
```
<your-github-organisation>/<your-repo-name-here>
```
as the `Repository name`. Do not initialise the repository with a `.gitignore`, licenses or a README, and ensure that you select a `Private` repository when prompted.

Finally, push your local repository to the repo you just created:
```
git remote add origin git@github.com:<your-github-organisation>/<your-repo-name-here>.git
git push -u origin main
```
