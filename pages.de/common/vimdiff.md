# vimdiff

> Öffne zwei oder mehr Dateien in Vim und zeige ihre Unterschiede an.
> Siehe auch `vim`.
> Weitere Informationen: <https://www.vim.org>.

- Öffne zwei Dateien und zeige ihre Unterschiede an:

`vimdiff {{pfad/zu/datei_1}} {{pfad/zu/datei_2}}`

- Bewege den Cursor zum linken|rechten Fenster:

`<Ctrl> + w {{h|l}}`

- Springe zum vorigen Unterschied:

`[c`

- Springe zum nächsten Unterschied:

`]c`

- Kopiere die hervorgehobenen Unterschiede vom anderen in das aktuelle Fenster:

`do`

- Kopiere die hervorgehobenen Unterschiede vom aktuellen in das andere Fenster:

`dp`

- Aktualisiere die hervorgehobenen Unterschiede und Textfaltungen:

`:diffupdate`

- Öffne/Schließe die Textfaltung unter dem Cursor:

`za`
