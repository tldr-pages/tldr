# lastcomm

> Zeige die zuletzt ausgeführten Befehle an.
> Weitere Informationen: <https://manpages.debian.org/stable/acct/lastcomm.1.en.html>.

- Gib Informationen zu allen Befehlen in acct aus (Aufzeichnungsdatei):

`lastcomm`

- Zeige die ausgeführten Befehle eines bestimmten Benutzers an:

`lastcomm --user {{benutzer}}`

- Zeige Informationen zu einem bestimmten Befehl an, der auf dem System ausgeführt wird:

`lastcomm --command {{befehl}}`

- Zeige Informationen zu Befehlen an, die auf einem bestimmten Terminal ausgeführt wurden:

`lastcomm --tty {{terminal_name}}`
