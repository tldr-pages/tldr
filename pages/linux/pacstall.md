# pacstall

> An AUR package manager for Ubuntu.
> More information: <https://github.com/pacstall/pacstall>.

- Search the package database for a package name:

`pacstall --search {{query}}`

- Install a package:

`pacstall --install {{package}}`

- Remove a package:

`pacstall --remove {{package}}`

- Add a repository to the database (only GitHub and GitLab are supported):

`pacstall --add-repo {{remote_repository_location}}`

- Update pacstall's scripts:

`pacstall --update`

- Update all packages:

`pacstall --upgrade`

- Display information about a package:

`pacstall --query-info {{package}}`

- List all installed packages:

`pacstall --list`
