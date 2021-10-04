# ssh-agent

> Erstelle einen SSH Agenten-Prozess.
> Ein SSH Agent behält die hinzugefügten SSH Schlüssel solange verschlüsselt im Arbeitsspeicher, bis diese entfernt werden oder der Agenten-Prozess beendet wird.
> Siehe auch `ssh-add`, um Schlüssel zu verwalten.
> Weitere Informationen: <https://man.openbsd.org/ssh-agent>.

- Starte einen SSH Agenten-Prozesses für die aktuelle Shell:

`eval $(ssh-agent)`

- Beende den aktuell laufenden SSH Agenten-Prozesses:

`ssh-agent -k`
