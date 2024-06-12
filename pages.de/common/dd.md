# dd

> Konvertiere und kopiere eine Datei.
> Weitere Informationen: <https://manned.org/man/dd.1p>.

- Erstelle ein bootbares USB-Laufwerk von einer isohybriden Datei (wie `archlinux-xxxx.iso`) und zeige den Fortschritt an:

`dd if={{pfad/zu/datei.iso}} of={{/dev/laufwerk}} status=progress`

- Klone ein USB-Laufwerk in ein anderes in 4MiB Blöcken, ignoriere Fehler und zeige den Fortschritt an:

`dd if={{/dev/quell_laufwerk}} of={{/dev/ziel_laufwerk}} bs=4M conv=noerror status=progress`

- Erstelle eine Datei mit 100 zufälligen Bytes mithilfe des Zufall-Treibers des Kernels:

`dd bs=100 count={{1}} if=/dev/urandom of={{pfad/zu/datei}}`

- Teste die Schreibgeschwindigkeit eines Laufwerks:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{pfad/zu/1GB_datei}}`

- Erstelle ein System-Backup als IMG Datei und zeige den Fortschritt an:

`dd if={{/dev/laufwerk}} of={{pfad/zu/datei.img}} status=progress`

- Stelle ein Laufwerk aus einer IMG Datei wieder her und zeige den Fortschritt an:

`dd if={{pfad/zu/datei.img}} of={{/dev/laufwerk}} status=progress`
