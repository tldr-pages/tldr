# pacstall

> An AUR package manager for Ubuntu.
> More information: <https://github.com/pacstall/pacstall>.

- Search the package database for a package name:

`pacstall {{[-S|--search]}} {{query}}`

- Install a package:

`pacstall {{[-I|--install]}} {{package}}`

- Remove a package:

`pacstall {{[-R|--remove]}} {{package}}`

- Add a repository to the database (only GitHub and GitLab are supported):

`pacstall {{[-A|--add-repo]}} {{remote_repository_location}}`

- Update pacstall's scripts:

`pacstall {{[-U|--update]}}`

- Update all packages:

`pacstall {{[-Up|--upgrade]}}`

- Display information about a package:

`pacstall {{[-Ci|--cache-info]}} {{package}}`

- List all installed packages:

`pacstall {{[-L|--list]}}`
