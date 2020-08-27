from github import Github

def create_pr_template(branch,pr_template,repo):
    file                 = open(pr_template,"r")
    pr_template_contents = file.read()
    try:
        repo.create_file(".github/PULL_REQUEST_TEMPLATE.md", "Added Pull Request Template", pr_template_contents, branch=branch)
        print("Create PR template ..")
    except Exception as e :
        print("PR template already exists..")

# create_pr_template("master","pull_request_template.md")

def configure_repo(name,repo) :
    repo.edit(has_wiki=False)
    print("Disabled wiki feature ..")

    repo.edit( delete_branch_on_merge=True)
    print("Enabled delete_on_merge feature ..")

    repo.get_branch('master').edit_protection(strict=True, enforce_admins=True, dismiss_stale_reviews=True, required_approving_review_count=1)
    # repo.get_branch('development').edit_protection(strict=True, enforce_admins=True, dismiss_stale_reviews=True, required_approving_review_count=1)
    
    print("Enabled branch protection rules ...")

# configure_repo("terraform-api-gateway")
       
def main():
    # g = Github("user", "password")
    g            = Github("your_access_token")
    repositories = ["terraform-api-gateway"]

    for repository in repositories:
        print("=========== Configuring Repository {} =================".format(repository))
        for repo in g.get_user().get_repos():
            if repo.name == repository:
                create_pr_template("master","pull_request_template.md",repo)
                # create_pr_template("development","pull_request_template.md",repo)
                configure_repo(repository,repo)
            else:
                pass
    print("============ COMPLETE =================")

if __name__ == "__main__":
    main()