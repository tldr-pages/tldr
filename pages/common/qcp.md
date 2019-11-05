# qcp

> Copy files with your favorite text editor.
> More information: <https://www.nongnu.org/renameutils/>.

- Copy a single file (invoke an editor with source on the left, target on the right):

`qcp {{source_file}}`

- Copy multiple JPG files:

`qcp {{*.jpg}}`

- Copy files, but swap the positions of the source and the target in the editor:

`qcp --option swap {{*.jpg}}`
