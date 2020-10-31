# ssh-agent

> Erstellt einen SSH Agenten-Prozess.
> Ein SSH Agent behält die hinzugefügten SSH Schlüssel solange verschlüsselt im Arbeitsspeicher, bis diese entfernt werden oder der Agenten-Prozess beendet wird.
> Hierfür wird im Folgenden das Programm `ssh-add` verwendet.

- Starten eines SSH Agenten-Prozesses für die aktuelle Shell:

`eval $(ssh-agent)`

- Beenden eines aktuell laufenden SSH Agenten-Prozesses:

`ssh-agent -k`
