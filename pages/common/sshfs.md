# SSHFS

> filesystem client based on ssh

- mounting remote directory

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- unmounting remote directory

`fusermount -u {{mountpoint}}`

- mounting remote directory from server with specific port

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- use compression

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`
