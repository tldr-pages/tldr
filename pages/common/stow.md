# stow

> Symlink manager.
> Often used to manage dotfiles.

- Symlink all files recursively to {{target}}:

`stow --target={{target}} {{file1 folder1 file2 folder2}}`

- Delete symlinks recursively from {{target}}:

`stow --delete --target={{target}} {{file1 folder1 file2 folder2}}`

- Simulate to see what the result would be like:

`stow  --simulate --target={{target}} {{file1 folder1 file2 folder2}}`

- Delete and resymlink:

`stow --restow --target={{target}} {{file1 folder1 file2 folder2}}`

- Exclude files matching a regular expression:

`stow  --ignore={{regex}} --target={{target}} {{file1 folder1 file2 folder2}}`
