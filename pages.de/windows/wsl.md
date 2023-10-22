# wsl

> Verwalte das Windows Subsystem für Linux von der Kommandozeile.
> Weitere Informationen: <https://learn.microsoft.com/windows/wsl/reference>.

- Starte eine Linux-Shell (in der Standard-Distribution):

`wsl {{shell_befehl}}`

- Führe einen Linux-Befehl aus, ohne eine Shell zu benutzen:

`wsl --exec {{befehl}} {{befehl_argumente}}`

- Gib eine bestimmte Distribution an:

`wsl --distribution {{distribution}} {{shell_befehl}}`

- Liste verfügbare Distributionen auf:

`wsl --list`

- Exportiere eine Distribution in eine `.tar` Datei:

`wsl --export {{distribution}} {{pfad/zu/datei.tar}}`

- Importiere eine Distribution von einer `.tar` Datei:

`wsl --import {{distribution}} {{pfad/zu/installations_verzeichnis}} {{pfad/zu/datei.tar}}`

- Ändere die WSL-Version einer bestimmten Distribution:

`wsl --set-version {{distribution}} {{version}}`

- Fahre das Windows Subsystem für Linux herunter:

`wsl --shutdown`
