# Github setup

This repository contains **simple python script** which setup github settings & branch protection rules. These are best practices followed on github.

## Install Python Dependencies

```
pip install PyGithub 
```

===
## Update Repository List in git_setup.py

In file git_setup.py *(line 29)*, update list of repositories, for which you want to setup rules.

**NOTE:** Uncomment *lines 22 & 36*, if you want to update PR template & branch protection rules in branch development as well.

===
## Run Python script

```
python git_setup.py
```

**Thank you..!!**
