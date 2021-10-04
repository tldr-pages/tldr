# pacstall

> An AUR package manager for Ubuntu.
> More information: <https://github.com/pacstall/pacstall>.

- Search the package database for a package name:

`pacstall --search {{package_name}}`

- Install a package:

`pacstall --install {{package_name}}`

- Remove program, equivalent of apt remove:

`pacstall --remove {{package_name}}`

- Add a repository to the database (only GitHub and GitLab are supported):

`pacstall --add-repo {{remote_repository_location}}`

- Update pacstall's scripts:

`pacstall --update`

- Update all packages:

`pacstall --upgrade`

- Show package info:

`pacstall -Qi {{package_name}}`

- List all installed packages:

`pacstall -L`
