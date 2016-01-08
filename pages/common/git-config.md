# git config

> Get and set repository or global options.

- Print list of options for current repository:

`git config --list --local`

- Print global list of options, set in ~/.gitconfig:

`git config --list --global`

- Get full list of options:

`git config --list`

- Get value of alias.ls option:

`git config alias.st`

- Set option alias.ls=status in file ~/.gitconfig:

`git config --global alias.ls "status"`

- Remove option alias.st from ~/.gitconfig:

`git config --global --unset alias.st`
