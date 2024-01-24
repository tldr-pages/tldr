# Chezmoi

> A multi-machine dotfile manager, written in Go.
> More information: <https://chezmoi.io>.

- Setup the destination directory:

`chezmoi init`

- Track a specific dotfile:

`chezmoi add {{path/to/dotfile}}`

- Edit the source state of a tracked dotfile:

`chezmoi edit {{path/to/dotfile_or_symlink}}`

- See pending changes:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Set up a destination directory from existing dotfiles of a Git repository:

`chezmoi init {{site}}/{{user}}/{{repo}}`

- Update from a remote repository:

`chezmoi update`
