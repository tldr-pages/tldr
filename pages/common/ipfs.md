# ipfs

> Inter Planetary File System.
> A peer-to-peer hypermedia protocol to make the web faster, safer, and more open.

- Save a remote file and give It a name but not pin It:

`ipfs get {{hash}} -o {{filename}}`

- Add a file from local to the File System with the filename _(-w)_, pin It and print the hash:
 
`ipfs add {{filename}} -w`

- Add a folder and files in It from local to the File System, pin It and print the hash:
 
`ipfs add -r {{folder}}`

- Pin a remote file, locally:

`ipfs pin add {{hash}}`

- Check pinned files:

`ipfs pin ls`

- Unpin a file from the local storage:

`ipfs pin rm {{hash}}`

- Create a new ipfs ID with a given name:

`ifps key gen --type=rsa --size=2048 {{name}}`

- Add an hash to the IPNS with the given ID _(omit --key for default)_. If is the hash of a folder, It will add the whole folder with files:

`ipfs name publish --key={{ID}} {{hash}}`

- Print a list of available keys:

`ipfs key list`

- Remove unpinned files from local storage:

`ipfs repo gc`
