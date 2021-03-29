# dd

> Konvertiere und kopiere eine Datei.
> Mehr Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- Erstelle ein bootbares USB-Laufwerk von einer isohybriden Datei (wie `archlinux-xxxx.iso`) und zeige den Fortschritt an:

`dd if={{pfad/zu/datei.iso}} of=/dev/{{usb_drive} status=progress`

- Klone ein USB-Laufwerk in ein anderes in 4MiB Blöcken, ignoriere Fehler und zeige den Fortschritt an:

`dd if=/dev/{{quell_laufwerk}} of=/dev/{{ziel_laufwerk}} bs=4M conv=noerror status=progress`

- Erstelle eine Datei mit 100 zufälligen Bytes mithilfe des Zufall-Treibers des Kernels:

`dd if=/dev/urandom of={{pfad/zu/datei}} bs=100 count=1`

- Teste die Schreibgeschwindigkeit eines Laufwerks:

`dd if=/dev/zero of={{pfad/zu/1GB_datei}} bs=1024 count=1000000`

- Überprüfe den Fortschritt eines laufenden dd-Prozsses (Führe diesen Befehl von einer anderen Shell aus):

`kill -USR1 $(pgrep ^dd)`
