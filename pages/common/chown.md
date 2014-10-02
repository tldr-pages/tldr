# chown

> Change the owning user/group of the specified files

- change the user of a file

`chown {{user}} {{path/to/file}}`

- change the user and group of a file
 
`chown {{user}}:{{group}} {{path/to/file}}`

- recursively change the owner of an entire folder

`chown -R {{user}} {{path/to/folder}}`

- change the owner of a symbolic link
 
`chown -h {{user}} {{path/to/symlink}}`

- use the owner and group of a reference file and apply those values to another file

`chown --reference={{reference-file}} {{path/to/file}}`
