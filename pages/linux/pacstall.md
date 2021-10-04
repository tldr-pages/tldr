# pacstall

> An AUR package manager for Ubuntu.
> More information: <https://github.com/pacstall/pacstall>.

- Search the package database for a package name:

`pacstall --search {{package_name}}`

- Install a package:

`pacstall --install {{package_name}}`

- Remove program, equivalent of apt remove:

`pacstall --remove {{package_name}}`

- Add one more repository to search:

`pacstall -A {{https://github/gitlab.com/example}}`

- Update pacstall's scripts:

`pacstall -U`

- Update packages, equivalent of apt upgrade:

`pacstall -Up`

- Show package info:

`pacstall -Qi {{package_name}}`

- List all installed packages:

`pacstall -L`
