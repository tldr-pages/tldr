# sshfs

> Filesystem client based on SSH.
> More information: <https://github.com/libfuse/sshfs/blob/master/sshfs.rst>.

- Mount remote directory:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{path/to/mount_point}}`

- Unmount remote directory:

`umount {{path/to/mount_point}}`

- Mount remote directory from server with specific port:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- Use compression:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`

- Follow symbolic links:

`sshfs -o follow_symlinks {{username}}@{{remote_host}}:{{remote_directory}} {{path/to/mount_point}}`
