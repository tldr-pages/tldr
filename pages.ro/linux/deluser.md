# deluser

> Ștergeți un utilizator din sistem.
> Notă: toate comenzile trebuie executate ca root.
> Mai multe informaţii: <https://manpages.debian.org/latest/adduser/deluser.html>

- Elimină un utilizator:

`deluser {{username}}`

- Eliminați un utilizator și directorul lor de acasă:

`deluser --remove-home {{username}}`

- Eliminați un utilizator și casa acestuia, dar copiați fișierele într-un fișier `.tar.gz” din directorul specificat:

`deluser --backup-to {{path/to/backup_directory}} --remove-home {{username}}`

- Eliminați un utilizator și toate fișierele deținute de acestea:

`deluser --remove-all-files {{username}}`
