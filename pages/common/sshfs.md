# SSHFS

> Filesystem client based on ssh.

- Mounting remote directory:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- Unmounting remote directory:

`fusermount -u {{mountpoint}}`

- Mounting remote directory from server with specific port:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- Use compression:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`
