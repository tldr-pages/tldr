# ipfs

> Inter Planetary File System.
> A peer-to-peer hypermedia protocol to make the web faster, safer, and more open.

- Save a remote file and give It a name but not pin It:

`ipfs get {{hash}} -o {{filename}}`

- Add a file from local to the file system with the filename (-w) and pin It:

`ipfs add {{filename}} -w`

- Add a folder and files in It from local to the File System and pin It:

`ipfs add -r {{folder}}`

- Pin a remote file, locally:

`ipfs pin add {{hash}}`

- Check pinned files:

`ipfs pin ls`

- Unpin a file from the local storage:

`ipfs pin rm {{hash}}`

- Remove unpinned files from local storage:

`ipfs repo gc`
