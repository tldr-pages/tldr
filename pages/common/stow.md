# stow

> Symlink manager.
> Often used to manage dotfiles.

- Symlink all files recursively to {{path/to/target_directory}}:

`stow --target={{directory}} {{file1 folder1 file2 folder2}}`

- Delete symlinks recursively from {{path/to/target_directory}}:

`stow --delete --target={{directory}} {{file1 folder1 file2 folder2}}`

- Simulate to see what the result would be like:

`stow --simulate --target={{directory}} {{file1 folder1 file2 folder2}}`

- Delete and resymlink:

`stow --restow --target={{directory}} {{file1 folder1 file2 folder2}}`

- Exclude files matching a regular expression:

`stow --ignore={{regex}} --target={{directory}} {{file1 folder1 file2 folder2}}`
