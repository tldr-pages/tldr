# chroot

> Führe einen Befehl oder eine interaktive Shell mit einem speziellen root-Verzeichnis aus.

- Führe einen Befehl mit einem neuen root-Verzeichnis aus:

`chroot {{pfad/zu/neuem/root}} {{befehl}}`

- Lege Benutzer und Gruppe (ID oder Name) fest, der benutzt werden soll:

`chroot --userspec={{benutzer:gruppe}}`
