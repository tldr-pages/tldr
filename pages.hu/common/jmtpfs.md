# jmtpfs

> FUSE-alapú fájlrendszer az MTP eszközök eléréséhez. További információ: <https://manned.org/jmtpfs>.

- MTP-eszköz csatlakoztatása egy könyvtárba:

`jmtpfs {{path/to/directory}}`

- Csatolási beállítások beállítása:

`jmtpfs -o {{allow_other,auto_unmount}} {{path/to/directory}}`

- Az elérhető MTP eszközök listája:

`jmtpfs --listDevices`

- Ha több eszköz is van, csatoljon egy adott eszközt:

`jmtpfs -device={{bus_id}},{{device_id}} {{path/to/directory}}`

- MTP eszköz függetlenítése:

`fusermount -u {{path/to/directory}}`
