# hub

> A wrapper for git that adds commands for working with github-based projects.
> The commands can also be used using "git" instead of "hub".

- Clone a repository you own, using just the repository name rather than the full URL:

`hub clone {{repo_name}}`

- Clone another user's repository, using their github username and the repository name:

`hub clone {{username}}/{{repo_name}}`

- Create a fork of the current repository (cloned from another user) under your github profile:

`hub fork`

- Create a PR of the current branch in the original repository (after pushing the branch to github):

`hub pull-request`

- Upload the current (local-only) repository to your github account:

`hub create`
