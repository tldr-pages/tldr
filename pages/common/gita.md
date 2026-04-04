# gita

> Manage multiple git repositories side by side.
> See also: `git`.
> More information: <https://github.com/nosarthur/gita>.

- Display a summary of a[ll] registered repositories:

`gita ll`

- Show the [st]atus of all registered repositories:

`gita st`

- Register repositories with gita:

`gita add {{path/to/repo1 path/to/repo2 ...}}`

- Pull updates for all registered repositories:

`gita pull`

- Run a git command on a specific repository:

`gita super {{repo_name}} {{git_command}}`

- Create a group of repositories and set it as the active context:

`gita group add {{[-n|--name]}} {{group_name}} {{repo1 repo2 ...}} && gita context {{group_name}}`

- Fetch updates for specific repositories or groups:

`gita fetch {{repo1 repo2 ...|group1 group 2 ...}}`

- Display information of all repositories:

`gita freeze`
