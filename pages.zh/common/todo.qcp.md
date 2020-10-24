# qcp

> Copy files using the default text editor to define the filenames.
> More information: <https://www.nongnu.org/renameutils/>.

- Copy a single file (open an editor with the source filename on the left and the target filename on the right):

`qcp {{source_file}}`

- Copy multiple JPG files:

`qcp {{*.jpg}}`

- Copy files, but swap the positions of the source and the target filenames in the editor:

`qcp --option swap {{*.jpg}}`
