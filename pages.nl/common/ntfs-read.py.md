# ntfs-read.py

> Een alleen-lezen NTFS verkenner voor het openen en extraheren van bestanden van NTFS volumes.
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Open een NTFS volume voor verkenning (bijvoorbeeld `C:\.\\` of `/dev/disk1s1`):

`ntfs-read.py {{volume}}`

- Haal een specifiek bestand uit een NTFS volume (bijvoorbeeld `\windows\system32\config\sam`):

`ntfs-read.py -extract {{\windows\system32\config\sam}} {{volume}}`

- Schakel debug-uitvoer in:

`ntfs-read.py -debug {{volume}}`

- Toon de help:

`ntfs-read.py --help`
