# ipfs

> Inter Planetary File System.
> A peer-to-peer hypermedia protocol to make the web faster, safer, and more open.
> More information: <https://ipfs.io>.

- Add a file from local to the file system, pin it and print the relative hash:

`ipfs add {{filename}}`

- Add a directory and its files recursively from local to the file system and print the relative hash:

`ipfs add -r {{directory}}`

- Save a remote file and give it a name but not pin it:

`ipfs get {{hash}} -o {{filename}}`

- Pin a remote file locally:

`ipfs pin add {{hash}}`

- Display pinned files:

`ipfs pin ls`

- Unpin a file from the local storage:

`ipfs pin rm {{hash}}`

- Remove unpinned files from local storage:

`ipfs repo gc`
