# hub

> A wrapper for Git that adds commands for working with GitHub-based projects.
> If set up as instructed by `hub alias`, one can use `git` to run `hub` commands.
> More information: <https://hub.github.com>.

- Clone a repository using its slug (owners can omit the username):

`hub clone {{username}}/{{repo_name}}`

- Create a fork of the current repository (cloned from another user) under your GitHub profile:

`hub fork`

- Push the current local branch to GitHub and create a PR for it in the original repository:

`hub push {{remote_name}} && hub pull-request`

- Create a PR of the current (already pushed) branch, reusing the message from the first commit:

`hub pull-request --no-edit`

- Create a new branch with the contents of a pull request and switch to it:

`hub pr checkout {{pr_number}}`

- Upload the current (local-only) repository to your GitHub account:

`hub create`

- Fetch Git objects from upstream and update local branches:

`hub sync`
