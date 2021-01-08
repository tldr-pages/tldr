# Chezmoi

> A multi-machine dotfile manager, written in Go.
> More information: <https://chezmoi.io>.

- Initialize chezmoi on your machine:

`chezmoi init`

- Tell chezmoi to manage a dotfile:

`chezmoi add {{path/to/file}}`

- Edit the source state of a tracked dotfile:

`chezmoi edit {{path/to/file}}`

- See changes chezmoi would make:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Set chezmoi up on another machine by downloading existing dotfiles from a Git repository:

`chezmoi init {{https://example.com/path/to/repository.git}}`

- Fetch the latest changes from a remote repository:

`chezmoi update`
