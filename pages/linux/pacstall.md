# pacstall

> Pacstall, make it easier to install AUR packages for Ubuntu.
> More information: <https://github.com/pacstall/pacstall>.

- Search for program in repositories, its equivalent of apt search:

`pacstall -S program`

- Install program, its the same of apt install:

`pacstall -I program`

- Remove program, its the same of apt remove:

`pacstall -R program`

- Add one more repository to search:

`pacstall -A {{https://github/gitlab.com/example}}`

- Update pacstall's scripts:

`pacstall -U`

- Update packages, its the same of apt upgrade:

`pacstall -Up`

- Show package info:

`pacstall -Qi {{packagename}}`

- List all packages are installed:

`pacstall -L`
