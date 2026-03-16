# gita

> Manage multiple git repositories side by side.
> See also: `git`.
> More information: <https://github.com/nosarthur/gita>.

- Display a summary of all registered repositories:

`gita ll`

- Show the status of all registered repositories:

`gita st`

- Register repositories with gita:

`gita add {{path/to/repo1}} {{path/to/repo2}}`

- Pull updates for all registered repositories:

`gita pull`

- Run a git command on a specific repository:

`gita super {{repo_name}} {{git_command}}`

- Create a group of repositories and set it as the active context:

`gita group add {{group_name}} {{repo1}} {{repo2}} && gita context {{group_name}}`

- Fetch updates for repositories in a specific group:

`gita fetch {{group_name}}`

- Export the current repository configuration:

`gita freeze`
