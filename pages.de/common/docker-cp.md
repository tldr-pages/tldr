# docker cp

> Kopiere Dateien oder Verzeichnisse zwischen Host- und Container-Dateisystem.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/cp>.

- Kopiere eine Datei oder ein Verzeichnis vom Host in einen Container:

`docker cp {{pfad/zu/datei_oder_verzeichnis_auf_host}} {{container_name}}:{{pfad/zu/datei_oder_verzeichnis_in_container}}`

- Kopiere eine Datei oder ein Verzeichnis von einem Container zum Host:

`docker cp {{container_name}}:{{pfad/zu/datei_oder_verzeichnis_in_container}} {{pfad/zu/datei_oder_verzeichnis_auf_host}}`

- Kopiere eine Datei oder ein Verzeichnis vom Host in einen Container und folge dabei Symlinks (kopiert die verlinkten Dateien statt der Symlinks):

`docker cp --follow-link {{pfad/zu/symlink_auf_host}} {{container_name}}:{{pfad/zu/datei_oder_verzeichnis_in_container}}`
