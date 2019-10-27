# qmv

> Move files and directories with your favorite text editor.
> More information: <https://www.nongnu.org/renameutils/>.

- Move a single file (invoke an editor with source on the left, target on the right):

`qmv {{source_file}}`

- Move multiple JPG files:

`qmv {{*.jpg}}`

- Move 3 directories:

`qmv -d {{path/to/dir_1}} {{path/to/dir_2}} {{path/to/dir_3}}`

- Move files/directories inside a directory:

`qmv -R {{path/to/directory}}`

- Move files, but swap the positions of the source and the target in the editor:

`qmv --option swap {{*.jpg}}`
