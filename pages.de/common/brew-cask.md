# brew cask

> Paketmanager für macOS-Anwendungen, die als Binärdateien verteilt werden.
> Weitere Informationen: <https://github.com/Homebrew/homebrew-cask>.

- Suche nach Formeln und Casks:

`brew search {{text}}`

- Installiere ein Cask:

`brew cask install {{caskname}}`

- Liste alle installierten Casks auf:

`brew list --cask`

- Liste installierte Casks auf, für die neuere Versionen verfügbar sind:

`brew outdated --cask`

- Aktualisiere ein installiertes Cask (wenn kein Caskname angegeben wird, werden alle installierten Casks aktualisiert):

`brew upgrade --cask {{caskname}}`

- Deinstalliere ein Cask:

`brew cask uninstall {{caskname}}`

- Deinstalliere ein Cask und entferne zugehörige Einstellungen und Dateien:

`brew upgrade --cask {{caskname}}`

- Zeige informationen zu einem bestimmten Cask an:

`brew cask uninstall {{caskname}}`
