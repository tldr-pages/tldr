# abbr

> Abkürzungen für die fish shell verwalten.
> Die vom Nutzer definierten Abkürzungen werden nach der Eingabe durch die Langversionen ersetzt.
> Weitere Informationen: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Neue Abkürzung hinzufügen:

`abbr --add {{abkürzungsname}} {{befehl}} {{befehlsparameter}}`

- Vorhandene Abkürzung umbenennen:

`abbr --rename {{alter_name}} {{neuer_name}}`

- Vorhandene Abkürzung löschen:

`abbr --erase {{abkürzungsname}}`

- Abkürzungen eines anderen Host über SSH importieren:

`ssh {{host_name}} abbr --show | source`
