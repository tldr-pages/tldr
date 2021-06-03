# alias

> Erstellt Aliasse - Alterative Namen für Befehle.
> Aliasse laufen mit der aktuellen Shell-Sitzung ab, es sei denn, sie werden in der Konfigurationsdatei der Shell definiert, z.B. `~/.bashrc`.
> Weitere Informationen: <https://tldp.org/LDP/abs/html/aliases.html>.

- Listet alle Aliasse auf:

`alias`

- Erstellt einen Alias:

`alias {{alias}}="{{befehl}}"`

- Zeigt den mit einem bestimmten Alias verknüpften Befehl an:

`alias {{alias}}`

- Entferne einen Alias:

`unalias {{alias}}`

- Macht `rm` zu einem interaktiven Befehl:

`alias {{rm}}="{{rm -i}}"`

- Erstellt den Alias `la` für `ls -a`:

`alias {{la}}="{{ls -a}}"`
