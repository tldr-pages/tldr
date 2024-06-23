# Chezmoi

> A multi-machine dotfile manager, written in Go.
> See also: `stow`, `tuckr`, `vcsh`, `homeshick`.
> More information: <https://chezmoi.io>.

- Setup up `chezmoi`, creating a Git repository in `~/.local/share/chezmoi`:

`chezmoi init`

- Set up `chezmoi` from existing dotfiles of a Git repository:

`chezmoi init {{repository_url}}`

- Start tracking one or more dotfiles:

`chezmoi add {{path/to/dotfile1 path/to/dotfile2 ...}}`

- Update repository with local changes:

`chezmoi re-add {{path/to/dotfile1 path/to/dotfile2 ...}}`

- Edit the source state of a tracked dotfile:

`chezmoi edit {{path/to/dotfile_or_symlink}}`

- See pending changes:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Pull changes from a remote repository and apply them:

`chezmoi update`
