# qmv

> Move files and directories using the default text editor to define the filenames.
> More information: <https://www.nongnu.org/renameutils/>.

- Move a single file (open an editor with the source filename on the left and the target filename on the right):

`qmv {{source_file}}`

- Move multiple JPEG files:

`qmv {{*.jpg}}`

- Move multiple directories:

`qmv -d {{path/to/directory1}} {{path/to/directory2}} {{path/to/directory3}}`

- Move all files and directories inside a directory:

`qmv --recursive {{path/to/directory}}`

- Move files, but swap the positions of the source and the target filenames in the editor:

`qmv --option swap {{*.jpg}}`

- Rename all files and folders in the current directory, but show only target filenames in the editor (you can think of it as a kind of simple mode):

`qmv --format=do .`
