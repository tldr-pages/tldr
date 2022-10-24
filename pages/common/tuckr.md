# tuckr

> Dotfile manager written in Rust
> More information: <https://github.com/RaphGL/Tuckr>.

- Check dotfile status:

`tuckr status`

- Add all dotfiles to system:

`tuckr add \*`

- Add all dotfiles except specified programs:

`tuckr add \* -e program1,program2

- Remove all dotfiles from system:

`tuckr rm \*`

- Add program dotfile and run its setup script:

`tuckr set program1`
