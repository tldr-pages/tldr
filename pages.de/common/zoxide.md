# zoxide

> Behält den Überblick über die am häufigsten verwendeten Verzeichnisse.
> Verwendet einen Ranking-Algorithmus, um zum besten Treffer zu navigieren.
> Weitere Informationen: <https://manned.org/zoxide>.

- Wechsel zu dem Verzeichnis mit dem höchsten Rang, das "foo" im Namen enthält:

`zoxide query {{foo}}`

- Wechsel in das höchstrangige Verzeichnis, das "foo" und danach "bar" enthält:

`zoxide query {{foo}} {{bar}}`

- Starte eine interaktive Verzeichnissuche (erfordert `fzf`):

`zoxide query --interactive`

- Füge ein Verzeichnis hinzu oder erhöhe seinen Rang:

`zoxide add {{path/to/directory}}`

- Entferne ein Verzeichnis aus der Datenbank von `zoxide`:

`zoxide remove {{path/to/directory}}`

- Generiere Shell-Konfigurationen für Befehls-Aliase (`z`, `za`, `zi`, `zq`, `zr`) für die angegebene Shell:

`zoxide init {{bash|fish|zsh}}`
