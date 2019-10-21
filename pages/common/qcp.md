# qcp

> Copy files with your favorite text editor.
> More information: <https://www.nongnu.org/renameutils/>

- Copy a single file (invoke an editor with source on the left, target on the right):

`qcp {{source_file}}`

- Copy multiple JPG files:

`qcp {{*.jpg}}`

- Copy files, but swap pattern in the editor -- target on the left and source on the right:

`qcp --option swap {{IMG-*.jpg}}`
