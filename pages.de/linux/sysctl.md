# sysctl

> Laufzeit-Kernelparameter auflisten und ändern.
> Weitere Informationen: <https://manned.org/sysctl.8>.

- Liste alle verfügbaren Kernelparameter mit ihren Werten auf:

`sysctl -a`

- Setze einen veränderbaren Kernelparameter:

`sysctl -w {{sektion.tunable}}={{wert}}`

- Frage aktuell geöffnete Datei-Handler ab:

`sysctl fs.file-nr`

- Frage die maximale Anzahl geöffneter Dateien ab:

`sysctl fs.file-max`

- Übernimm Änderungen aus der `/etc/sysctl.conf` Datei:

`sysctl -p`
