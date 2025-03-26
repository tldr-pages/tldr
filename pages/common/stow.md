# stow

> Symlink manager.
> Often used to manage dotfiles.
> See also: `chezmoi`, `tuckr`, `vcsh`, `homeshick`.
> More information: <https://www.gnu.org/software/stow/manual/html_node/Invoking-Stow.html>.

- Symlink all files recursively to a given directory:

`stow {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Delete symlinks recursively from a given directory:

`stow {{[-D|--delete]}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Simulate to see what the result would be like:

`stow {{[-n|--simulate]}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Delete and resymlink:

`stow {{[-R|--restow]}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Exclude files matching a regular expression:

`stow --ignore={{regular_expression}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`
