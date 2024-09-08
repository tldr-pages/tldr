# tuckr

> Dotfile manager written in Rust.
> See also: `chezmoi`, `vcsh`, `homeshick`, `stow`.
> More information: <https://github.com/RaphGL/Tuckr>.

- Check dotfile status:

`tuckr status`

- Add all dotfiles to system:

`tuckr add \*`

- Add all dotfiles except specified programs:

`tuckr add \* -e {{program1}},{{program2}}`

- Remove all dotfiles from the system:

`tuckr rm \*`

- Add a program dotfile and run its setup script:

`tuckr set {{program}}`
