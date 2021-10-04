# adduser

> Tool um Benutzer hinzuzufügen.
> Weitere Informationen: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Erstelle einen neuen Benutzer mit einem Standard-Home-Verzeichnis und Aufforderung an den Benutzer, ein Passwort festzulegen:

`adduser {{benutzername}}`

- Erstelle einen neuen Benutzer ohne Home-Verzeichnis:

`adduser --no-create-home {{benutzername}}`

- Erstelle einen neuen Benutzer mit einem Home-Verzeichnis unter dem angegebenen Pfad:

`adduser --home {{pfad/zu/home}} {{benutzername}}`

- Erstelle einen neuen Benutzer, bei dem die angegebene Shell als Anmeldeshell eingestellt ist:

`adduser --shell {{pfad/zu/shell}} {{benutzername}}`

- Erstelle einen neuen Benutzer und füge ihn zur angegebenen Gruppe hinzu:

`adduser --ingroup {{gruppe}} {{benutzername}}`

- Füge einen vorhandenen Benutzer zur angegebenen Gruppe hinzu:

`adduser {{benutzername}} {{gruppe}}`
