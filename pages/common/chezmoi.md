# Chezmoi

> A multi-machine dotfile manager, written in Go.
> More information: <https://github.com/twpayne/chezmoi>.

- Initialize chezmoi on your machine:

`chezmoi init`

- Tell chezmoi to manage a dotfile:

`chezmoi add ~/.zshrc`

- Edit the source state of a tracked dotfile:

`chezmoi edit ~/.bashrc

- See changes chezmoi would make:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

## Using chezmoi across multiple machines

- Setting chezmoi up on another machine, from a service like GitHub:

`chezmoi init {{https://git_url}}`

- Fetch latest changes from a remote repo:

`chezmoi update`
