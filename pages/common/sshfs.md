# [sshfs](http://man7.org/linux/man-pages/man1/sshfs.1.html)
> Filesystem client based on ssh.

- Mount remote directory:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- Unmount remote directory:

`fusermount -u {{mountpoint}}`

- Mount remote directory from server with specific port:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- Use compression:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`
