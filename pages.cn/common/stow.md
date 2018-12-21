# stow

> Symlink manager.
> Often used to manage dotfiles.

- Symlink all files recursively to a given directory:

`stow --target={{path/to/target_directory}} {{file1 folder1 file2 folder2}}`

- Delete symlinks recursively from a given directory:

`stow --delete --target={{path/to/target_directory}} {{file1 folder1 file2 folder2}}`

- Simulate to see what the result would be like:

`stow --simulate --target={{path/to/target_directory}} {{file1 folder1 file2 folder2}}`

- Delete and resymlink:

`stow --restow --target={{path/to/target_directory}} {{file1 folder1 file2 folder2}}`

- Exclude files matching a regular expression:

`stow --ignore={{regex}} --target={{path/to/target_directory}} {{file1 folder1 file2 folder2}}`
