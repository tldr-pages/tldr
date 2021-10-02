# adduser

> Tool um Benutzer hinzuzufügen.
> Mehr Informationen: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Erzeugen eines neuen Benutzers mit einem Standard-Home-Verzeichnis und Aufforderung an den Benutzer, ein Passwort festzulegen:

`adduser {{benutzername}}`

- Erzeugen eines neuen Benutzers ohne Home-Verzeichnis:

`adduser --no-create-home {{benutzername}}`

- Erzeugen eines neuen Benutzers mit einem Home-Verzeichnis unter dem angegebenen Pfad:

`adduser --home {{pfad/zu/home}} {{benutzername}}`

- Erzeugen eines neuen Benutzers, bei dem die angegebene Shell als Anmeldeshell eingestellt ist:

`adduser --shell {{path/to/shell}} {{username}}`

- Erzeugen eines neuen Benutzers, der zur angegebenen Gruppe gehört:

`adduser --ingroup {{gruppe}} {{benutzername}}`

- Hinzufügen eines vorhandenen Benutzers zur angegebenen Gruppe:

`adduser {{username}} {{group}}`
