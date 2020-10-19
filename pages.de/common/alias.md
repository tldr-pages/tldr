# alias

> Erstellt Aliase - Wörter, die durch eine Befehlszeile ersetzt werden.
> Aliase laufen mit der aktuellen Shell-Sitzung ab, es sei denn, sie sind in der Konfigurationsdatei der Shell definiert, z.B. `~/.bashrc`.

- Listet alle Aliase auf:

`alias`

- Erstellt einen Alias:

`alias {{wort}}="{{befehl}}"`

- Zeigt den mit einem bestimmten Alias verknüpften Befehl an:

`alias {{wort}}`

- Entferne einen Alias:

`unalias {{wort}}`

- Macht `rm` zu einem interaktiven Befehl:

`alias {{rm}}="{{rm -i}}"`

- Erstellt `la` als Abkürzung für `ls -a`:

`alias {{la}}="{{ls -a}}"`
