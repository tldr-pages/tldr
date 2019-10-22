# qmv

> Move files and directories with your favorite text editor.
> More information: <https://www.nongnu.org/renameutils/>.

- Move a single file (invoke an editor with source on the left, target on the right):

`qmv {{source_file}}`

- Move multiple JPG files:

`qmv {{*.jpg}}`

- Move directories:

`qmv -d {{directory/}} {{another_directory/}} {{the_other_directory/}}`

- Move files/directories inside a directory:

`qmv -R {{directory/}}`

- Move files, but swap pattern in the editor -- target on the left and source on the right:

`qmv --option swap {{*.jpg}}`
