# Chezmoi

> A multi-machine dotfile manager, written in Go.
> More information: <https://github.com/twpayne/chezmoi>.

- Initialize chezmoi on your machine:

`chezmoi init`

- Tell chezmoi to manage a dotfile:

`chezmoi add {{path_to_file}}`

- Edit the source state of a tracked dotfile:

`chezmoi edit {{path_to_file}}

- See changes chezmoi would make:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Set chezmoi up on another machine, from a service like GitHub:

`chezmoi init {{https://git_url}}`

- Fetch latest changes from a remote repo:

`chezmoi update`
