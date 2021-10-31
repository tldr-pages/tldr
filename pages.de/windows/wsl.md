# wsl

> Verwalte das Windows Subsystem für Linux von der Kommandozeile.
> Weitere Informationen: <https://docs.microsoft.com/windows/wsl/reference>.

- Starte eine Linux-Shell (in der Standard-Distribution):

`wsl {{shell_kommando}}`

- Führe ein Linux-Kommando aus ohne eine Shell zu benutzen:

`wsl --exec {{kommando}} {{kommando_argumente}}`

- Gib eine bestimmte Distribution an:

`wsl --distribution {{distribution}} {{shell_kommando}}`

- Liste verfügbare Distributionen auf:

`wsl --list`

- Exportiere eine Distribution in eine `.tar` Datei:

`wsl --export {{distribution}} {{pfad/zu/tar_datei.tar}}`

- Importiere eine Distribution von einer `.tar` Datei:

`wsl --import {{distribution}} {{pfad/zu/installations_ordner}} {{pfad/zu/tar_datei.tar}}`

- Ändere die WSL-Version einer bestimmten Distribution:

`wsl --set-version {{distribution}} {{version}}`

- Fahre das Windows Subsystem für Linux herunter:

`wsl --shutdown`
