# sshfs

> Client sistem de fișiere bazat pe ssh.
> Mai multe informaţii: <https://github.com/libfuse/sshfs>

- Montează directorul de la distanță:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- Demontați directorul de la distanță:

`umount {{mountpoint}}`

- Montați directorul de la distanță de la server cu port specific:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- Foloseşte compresia:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`

- Urmați link-uri simbolice:

`sshfs -o follow_symlinks {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`
