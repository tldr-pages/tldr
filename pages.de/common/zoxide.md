# zoxide

> Behält den Überblick über die am häufigsten verwendeten Verzeichnisse.
> Verwendet einen Ranking-Algorithmus, um zum besten Treffer zu navigieren.
> Weitere Informationen: <https://manned.org/zoxide>.

- Wechsel zu dem Verzeichnis mit dem höchsten Rang, das `string` im Namen enthält:

`zoxide query string`

- Wechsel in das höchstrangige Verzeichnis, das `string1` und dann `string2` enthält:

`zoxide query string1 string2`

- Starte eine interaktive Verzeichnissuche (erfordert `fzf`):

`zoxide query {{[-i|--interactive]}}`

- Füge ein Verzeichnis hinzu oder erhöhe seinen Rang:

`zoxide add {{path/to/directory}}`

- Entferne ein Verzeichnis aus der Datenbank von `zoxide`:

`zoxide remove {{path/to/directory}}`

- Generiere Shell-Konfigurationen für Befehls-Aliase (`z`, `zi`) für die angegebene Shell:

`zoxide init {{bash|elvish|fish|nushell|posix|powershell|tcsh|xonsh|zsh}}`
