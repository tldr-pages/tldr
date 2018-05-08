# ipfs

> Inter Planetary File System.
> A peer-to-peer hypermedia protocol to make the web faster, safer, and more open.

- Add a file from local to the file system and pin It:

`ipfs add {{filename}}`

- Add a folder and its files recursively from local to the File System:

`ipfs add -r {{folder}}`

- Save a remote file and give It a name but not pin It:

`ipfs get {{hash}} -o {{filename}}`

- Pin a remote file locally:

`ipfs pin add {{hash}}`

- Display pinned files:

`ipfs pin ls`

- Unpin a file from the local storage:

`ipfs pin rm {{hash}}`

- Remove unpinned files from local storage:

`ipfs repo gc`
