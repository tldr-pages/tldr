# pacstall

> An AUR package manager for Ubuntu.
> More information: <https://github.com/pacstall/pacstall>.

- Search for program in repositories, its equivalent of apt search:

`pacstall -S program`

- Install program, equivalent of apt install:

`pacstall -I program`

- Remove program, equivalent of apt remove:

`pacstall -R program`

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
