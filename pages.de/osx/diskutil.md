# diskutil

> Dienstprogramm zur Verwaltung lokaler Festplatten und Volumes.
> Weitere Informationen: <https://ss64.com/osx/diskutil.html>.

- Auflisten aller aktuell verfügbaren Festplatten, Partitionen und gemounteten Volumes:

`diskutil list`

- Reparieren der Dateisystem-Datenstrukturen eines Volumes:

`diskutil repairVolume {{/dev/diskX}}`

- Einen Datenträger aushängen:

`diskutil unmountDisk {{/dev/diskX}}`

- Eine CD/DVD auswerfen (zuerst aushängen):

`diskutil eject {{/dev/disk1}}`
