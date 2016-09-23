# hub

> A command-line wrapper for git that makes you better at GitHub.
> The commands can also be used using "git" instead of "hub".

- Clone a repository you own:

`hub clone {{repo_name}}`

- Clone another user's repository:

`hub clone {{github_username}}/{{repo_name}}`

- Fork your own copy of a repository cloned from another user (must be in the cloned repository folder, creates a remote named after your GitHub username):

`hub fork`

- Create a pull request from your fork (first pushing the changes to your fork remote, named after your GitHub username):

`git push {{your_github_username}} {{current_branch}} && hub pull-request`

- Open the current project's issues page:

`hub browse -- issues`
