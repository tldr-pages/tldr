# snapper

> A fájlrendszer pillanatkép-kezelő eszköz. További információ: <http://snapper.io/manpages/snapper.html>.

- Pillanatkép konfigurációk listázása:

`snapper list-configs`

- Snapper konfiguráció létrehozása:

`snapper -c {{config}} create-config {{path/to/directory}}`

- Pillanatfelvétel létrehozása leírással:

`snapper -c {{config}} create -d "{{snapshot_description}}"`

- Pillanatképek listázása egy konfigurációhoz:

`snapper -c {{config}} list`

- Pillanatkép törlése:

`snapper -c {{config}} delete {{snapshot_number}}`

- Pillanatképek tartományának törlése:

`snapper -c {{config}} delete {{snapshot_X}}-{{snapshot_Y}}`
