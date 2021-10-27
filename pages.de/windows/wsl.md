# wsl

> Verwalte das Windows Subsystem für Linux von der Kommandozeile.
> Weitere Informationen: <https://docs.microsoft.com/windows/wsl/reference>.

- Starte eine Linux-Shell (in der Standard-Distribution):

`wsl {{shell_command}}`

- Führe ein Linux-Kommando aus ohne eine Shell zu benutzen:

`wsl --exec {{command}} {{command_arguments}}`

- Gib eine bestimmte Distribution an:

`wsl --distribution {{distribution}} {{shell_command}}`

- Liste verfügbare Distributionen auf:

`wsl --list`

- Exportiere eine Distribution in eine `.tar` Datei:

`wsl --export {{distribution}} {{path/to/distro_fs.tar}}`

- Importiere eine Distribution von einer `.tar` Datei:

`wsl --import {{distribution}} {{path/to/install_location}} {{path/to/distro_fs.tar}}`

- Ändere die WSL-Version einer bestimmten Distribution:

`wsl --set-version {{distribution}} {{version}}`

- Fahre das Windows Subsystem für Linux herunter:

`wsl --shutdown`
