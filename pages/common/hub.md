# hub

> A command-line wrapper for git that makes you better at GitHub.
> The commands can also be used using "git" instead of "hub".

- Clone a repository you own:

`hub clone {{repo_name}}`

- Clone another user repository:

`hub clone {{github_username}}/{{repo_name}}`

- Fork repository cloned from another user to your user:

`hub fork`

- Create a pull request from your fork:

`git pull {{github_username}} && hub pull-request`

- Open the current project's issues page:

`hub browse -- issues`
