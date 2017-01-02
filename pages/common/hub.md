# hub

> A wrapper for git that adds commands for working with github-based projects.
> The commands can also be used using "git" instead of "hub".

- Clone a repository you own, using just the repository name rather than the full URL:

`hub clone {{repo_name}}`

- Clone another user's repository, using their github username and the repository name:

`hub clone {{username}}/{{repo_name}}`

- Create a fork of the current repository (cloned directly from another user) under your github profile:

`hub fork`

- Create a pull request of the current branch in the upstream project (after sending the changes to your fork on github):

`hub pull-request`

- Upload the current repository to your github account:

`hub create`
