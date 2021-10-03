# sysctl

> Laufzeit-Kernelparameter auflisten und ändern.

- Liste alle verfügbaren Kernelparameter mit ihren Werten auf:

`sysctl -a`

- Setze einen veränderbaren Kernelparameter:

`sysctl -w {{sektion.tunable}}={{Wert}}`

- Aktuell geöffnete Datei-Handle (Filehandle) abfragen:

`sysctl fs.file-nr`

- Frage maximale Anzahl geöffneter Dateien ab:

`sysctl fs.file-max`

- Änderungen aus der `/etc/sysctl.conf` Datei übernehmen:

`sysctl -p`
