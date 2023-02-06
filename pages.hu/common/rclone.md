# rclone

> CLI program fájlok és könyvtárak másolására/szinkronizálására/mozgatására számos felhőszolgáltatásba és onnan. További információ: <https://rclone.org>.

- Egy rclone távoli könyvtár tartalmának listázása:

`rclone lsf {{remote_name}}:{{path/to/directory}}`

- Fájl vagy könyvtár másolása helyi forrásból távoli célállomásra:

`rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/destination_directory}}`

- Fájl vagy könyvtár másolása távoli forrásból helyi célállomásra:

`rclone copy {{remote_name}}:{{path/to/source_file_or_directory}} {{path/to/destination_directory}}`

- Helyi forrás szinkronizálása távoli célállomással, csak a célállomás módosítása:

`rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Fájl vagy könyvtár áthelyezése helyi forrásból távoli célállomásra:

`rclone move {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Távoli fájl vagy könyvtár törlése (teszteléshez használja a `--dry-run` címet, a tényleges törléshez távolítsa el):

`rclone --dry-run delete {{remote_name}}:{{path/to/file_or_directory}}`

- Mount rclone remote (kísérleti):

`rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}`

- Unmount rclone remote, ha a CTRL-C sikertelen (kísérleti):

`fusermount -u {{path/to/mount_point}}`
