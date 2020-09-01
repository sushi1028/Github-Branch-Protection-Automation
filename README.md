# GITHUB BRANCH PROTECTION USING PYTHON API

This repository contains **python script** which enable important github settings & branch protection rules (according to git best practices). This script automate following stuff for us -

1. Disable **wiki**
2. Enable **auto delete head brancheson merge**
3. Include **PR** Template
4. Turn on **Require pull request reviews before merging**, with 1 required approval
5. Turn on **Dismiss stale pull request approvals when new commits are pushed**
6. Turn on **Require status checks to pass before merging**
7. Turn on **Require branches to be up to date before merging**
8. Turn on **Include administrators**"


# LETS GET STARTED

## Install Python Dependencies

```
pip install PyGithub 
```

---
## Update Repository List in git_setup.py

In code file, git_setup.py (line 29), update list of repositories, for which you want to setup above rules.

**NOTE:** Uncomment or Add branches (lines 22 & 36), if you want to update PR template & apply branch protection rules in branch development(or any other branches) as well.

---
## Run Python Code

```
python git_setup.py
```

**Thank you..!!**
