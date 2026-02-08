# umount

> Löse ein Dateisystem von seinem Mount Point und mache es nicht mehr zugänglich.
> Ein Dateisystem kann nicht ausgehängt werden, wenn es belegt ist.
> Weitere Informationen: <https://man.openbsd.org/umount>.

- Hänge ein Dateisystem aus, indem du den Pfad zur Quelle übergibt, von der es gemountet ist:

`umount {{pfad/zu/gerätedatei}}`

- Hänge ein Dateisystem aus, indem du den Pfad zum Ziel übergibt, an dem es gemountet ist:

`umount {{pfad/zu/mounted_verzeichnis}}`

- Hänge alle gemounteten Dateisysteme aus (außer dem `proc`-Dateisystem):

`umount -a`
