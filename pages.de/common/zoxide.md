# zoxide

> Keep track of the most frequently used directories.
> Uses a ranking algorithm to navigate to the best match.
> Weitere Informationen: <https://github.com/ajeetdsouza/zoxide>.

- Wechsel zu dem Verzeichnis mit dem höchsten Rang, das "foo" im Namen enthält:

`zoxide query {{foo}}`

- Wechsel in das höchstrangige Verzeichnis, das "foo" und dann "bar" enthält:

`zoxide query {{foo}} {{bar}}`

- Starte eine interaktiven Verzeichnissuche (erfordert `fzf`):

`zoxide query --interactive`

- Füge ein Verzeichniss hinzu oder erhöhe seinen Rang:

`zoxide add {{path/to/directory}}`

- Entferne interaktiv ein Verzeichniss aus der Datenbank von `zoxide`:

`zoxide remove {{path/to/directory}} --interactive`

- Generiere Shell-Konfigurationen für Befehls-Aliase (`z`, `za`, `zi`, `zq`, `zr`):

`zoxide init {{bash|fish|zsh}}`
