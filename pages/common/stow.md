# stow

> Symlink manager.
> Often used to manage dotfiles.
> See also: `chezmoi`, `tuckr`, `vcsh`, `homeshick`.
> More information: <https://www.gnu.org/software/stow/manual/stow.html#Invoking-Stow>.

- Symlink all files recursively to a given directory:

`stow {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Delete symlinks recursively from a given directory:

`stow {{[-D|--delete]}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Simulate to see what the result would be like:

`stow {{[-n|--simulate]}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Delete and resymlink:

`stow {{[-R|--restow]}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Exclude files matching a `regex`:

`stow --ignore={{regex}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
