# sshfs

> SSH-alapú fájlrendszer-kliens. További információ: <https://github.com/libfuse/sshfs>.

- Távoli könyvtár csatlakoztatása:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- Távoli könyvtár leválasztása:

`umount {{mountpoint}}`

- Távoli könyvtár mountolása a szerverről egy adott porton:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- Tömörítés használata:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`

- Szimbolikus linkek követése:

`sshfs -o follow_symlinks {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`
