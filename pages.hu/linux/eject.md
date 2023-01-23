# eject

> CD-k, floppylemezek és szalagos meghajtók kivetítése. További információ: <https://manned.org/eject>.

- Az alapértelmezett eszköz megjelenítése:

`eject -d`

- Az alapértelmezett eszköz kidobása:

`eject`

- Egy adott eszköz kidobása (az alapértelmezett sorrend: cd-rom, scsi, floppy és szalag):

`eject {{/dev/cdrom}}`

- Átkapcsolja, hogy egy eszköz tálcája nyitva vagy zárva van-e:

`eject -T {{/dev/cdrom}}`

- A cd meghajtó kiürítése:

`eject -r {{/dev/cdrom}}`

- Floppy meghajtó kioldása:

`eject -f {{/mnt/floppy}}`

- Szalagmeghajtó kioldása:

`eject -q {{/mnt/tape}}`
