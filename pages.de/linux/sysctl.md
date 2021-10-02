# sysctl

> Kernelparameter zur Laufzeit auflisten und ändern. Als Parameter stehen die Werte unter `/proc/sys/` zur Verfügung (in Unterordner organisiert).

- Liste alle verfügbaren Kernelparameter mit ihren Werten auf:

`sysctl -a`

- Setze einen veränderbaren Kernelparameter:

`sysctl -w {{Sektion.tunable}}={{Wert}}`

- Aktuell geöffnete Datei-Handle (Filehandle) abfragen:

`sysctl fs.file-nr`

- Frage maximale Anzahl geöffneter Dateien ab:

`sysctl fs.file-max`

- Änderungen aus der `/etc/sysctl.conf` Datei übernehmen:

`sysctl -p`
